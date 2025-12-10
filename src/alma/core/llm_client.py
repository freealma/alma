from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import List, Dict, Any, Optional
import json
from ..utils.config import config

class LLMClient:
    def __init__(self):
        config.validate()
        
        self.llm = ChatDeepSeek(
            model=config.DEFAULT_MODEL,
            temperature=config.DEFAULT_TEMPERATURE,
            max_tokens=config.MAX_TOKENS,
            api_key=config.DEEPSEEK_API_KEY,
            base_url=config.DEEPSEEK_API_BASE
        )
        
        # System prompt
        self.system_prompt = """Eres Alma, un asistente AI conversacional con memoria de corto plazo.
        
        Tienes acceso a un sistema de memoria donde se almacenan conversaciones pasadas y contexto.
        
        Instrucciones:
        1. Usa las memorias como contexto para entender la conversación actual
        2. Formula respuestas nuevas y originales basadas en el contexto
        3. Sé conciso pero útil en tus respuestas
        4. Si algo no está claro en las memorias, pregunta para aclarar
        5. Mantén un tono amigable y profesional
        
        Memorias relevantes:
        {memories_context}
        
        Responde en el mismo idioma que el usuario utiliza."""
    
    def format_memories_context(self, memories: List[Dict]) -> str:
        """Format memories into context string"""
        if not memories:
            return "No hay memorias previas relevantes para esta conversación."
        
        context_lines = []
        for mem in memories:
            if isinstance(mem, tuple):
                # Handle tuple format from database
                key, value, scope, timestamp = mem
                context_lines.append(f"- {key}: {value} (Scope: {scope}, Time: {timestamp})")
            else:
                # Handle dict format
                context_lines.append(f"- {mem.get('key', 'Unknown')}: {mem.get('value', '')}")
        
        return "\n".join(context_lines)
    
    def generate_response(self, 
                         user_message: str, 
                         memories: List[Dict] = None,
                         conversation_history: List[Dict] = None) -> Dict[str, Any]:
        """Generate a response using LLM with memory context"""
        
        # Format memories context
        memories_context = self.format_memories_context(memories or [])
        
        # Create prompt with system message
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=self.system_prompt.format(
                memories_context=memories_context
            )),
            MessagesPlaceholder(variable_name="conversation_history"),
            HumanMessage(content=user_message)
        ])
        
        # Prepare conversation history
        history_messages = []
        if conversation_history:
            for msg in conversation_history[-10:]:  # Last 10 messages for context
                if msg["role"] == "user":
                    history_messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    history_messages.append(AIMessage(content=msg["content"]))
        
        # Generate response
        chain = prompt | self.llm
        response = chain.invoke({
            "conversation_history": history_messages
        })
        
        return {
            "content": response.content,
            "model": config.DEFAULT_MODEL,
            "tokens_used": None  # DeepSeek API doesn't return token count directly
        }
    
    def test_connection(self) -> bool:
        """Test connection to LLM API"""
        try:
            test_prompt = ChatPromptTemplate.from_messages([
                HumanMessage(content="Hello, respond with 'OK' if you can hear me.")
            ])
            chain = test_prompt | self.llm
            response = chain.invoke({})
            return "OK" in response.content.upper()
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False

# Singleton instance
llm_client = LLMClient()