
# 🚀 ESTÁNDARES GIT - ALMA

## 📁 RAMAS - CÓMO ORGANIZARSE

### Las ramas que usamos:
```
main       → Lo que está en producción (ESTABLE)
develop    → Donde juntamos todo lo nuevo
feature/*  → Cada cosa nueva que desarrollamos
hotfix/*   → Arreglos urgentes de producción
```

### Cómo ponerles nombre:
```bash
# Bien claro y específico
feature/ALMA-15-sistema-login
hotfix/ALMA-89-error-critico
feature/ALMA-34-mejorar-memoria
```

## 💾 COMMITS - CÓMO GUARDAR CAMBIOS

### Commits Normales (usar 80% del tiempo):
```bash
feat(auth): agregar login básico
fix(memory): resolver leak de memoria  
docs(api): actualizar documentación
refactor: mejorar código existente
```

### Commits Largos (cuando necesitas explicar):
```bash
feat(security): implementar autenticación completa

- Agregar login con usuario/contraseña
- Implementar recuperación de cuenta
- Añadir verificación por email
- Configurar tiempos de expiración

Resuelve: #ALMA-15
```

### 🤔 ¿CUÁNDO USAR CADA UNO?

| Situación | Tipo de Commit | Ejemplo |
|-----------|----------------|---------|
| **Cambio pequeño** | ✅ Normal | `fix: corregir typo` |
| **Funcionalidad nueva** | ✅ Normal | `feat: agregar botón` |
| **Algo complejo** | ✅ Largo | **Varias partes que explican** |
| **Muchos archivos** | ✅ Largo | **Necesitas contexto** |

## 🔄 CÓMO TRABAJAR DÍA A DÍA

### 1. EMPEZAR NUEVA FEATURE:
```bash
# Actualizarse
git checkout develop
git pull origin develop

# Crear rama nueva
git checkout -b feature/ALMA-15-mi-feature-genial
```

### 2. TRABAJAR Y GUARDAR:
```bash
# Guardar seguido (sin miedo)
git add .
git commit -m "feat: empezar feature"
git commit -m "feat: agregar parte 1" 
git commit -m "fix: corregir error"
git commit -m "feat: terminar feature"
```

### 3. TERMINAR Y SUBIR:
```bash
# Subir cambios
git push origin feature/ALMA-15-mi-feature-genial

# Crear Pull Request en GitHub/GitLab
# Esperar que alguien revise
# Mergear a develop cuando esté aprobado
```

## 🚨 CASOS ESPECIALES

### Arreglo URGENTE en producción:
```bash
git checkout main
git pull origin main
git checkout -b hotfix/ALMA-99-error-grave
# Arreglar el problema
git commit -m "fix: resolver error crítico"
git checkout main
git merge hotfix/ALMA-99-error-grave
```

### Estructura Inicial del Proyecto:
```bash
git checkout -b feature/ALMA-01-estructura-inicial
# Crear todas las carpetas y archivos base
git add .
git commit -m "feat: crear estructura inicial del proyecto"
git checkout develop
git merge feature/ALMA-01-estructura-inicial
```

## 🎯 REGLAS BÁSICAS - NO OLVIDAR

### ✅ HACER:
- Commits seguidos y pequeños
- Nombres claros en ramas
- Trabajar siempre en ramas nuevas
- Actualizar develop antes de empezar

### ❌ NO HACER:
- Commits gigantes de 3 días
- Trabajar directo en main/develop
- Olvidar poner números de ticket
- Subir código que no compila

## 🔧 COMANDOS ÚTILES QUE SÍ USARÁS

```bash
# Ver estado rápido
git status
git log --oneline -5

# Ver ramas
git branch
git branch -a

# Actualizar rama
git fetch
git pull origin develop

# Guardar cambios temporales (por si te interrumpen)
git stash
git stash pop
```

## 💡 RECUERDA:
**Git es tu amigo, no tu enemigo.**
**Mejor muchos commits pequeños que uno gigante.**
**Las ramas son gratis - úsalas sin miedo.**

---
*Última actualización: [fecha]*


## 📁 **¿DÓNDE GUARDAR ESTE ARCHIVO?**

```bash
# En la raíz de tu proyecto
tu-proyecto/
├── GIT_STANDARDS.md    # ← Este archivo
├── README.md
├── src/
└── package.json
```

## 🎯 **¿POR QUÉ ESTE ARCHIVO ES MEJOR?**

- **✅ Simple** - Sin tecnicismos innecesarios
- **✅ Práctico** - Solo lo que realmente usarás
- **✅ Claro** - Explicado para humanos normales
- **✅ Útil** - Con ejemplos que copiar/pegar

## 🔄 **ACTUALIZACIÓN FUTURA:**

Cuando domines esto, podemos agregar:
- Flujo de releases
- Estrategias de deploy
- Herramientas automáticas
- Workflows de equipo

**¿Te gusta así de simple? ¿O quieres que ajustemos algo más?**