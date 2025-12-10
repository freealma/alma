# 🚀 ESTÁNDARES GIT - ALMA (VERSIÓN DEFINITIVA)

## 🌊 FLUJO DE TRABAJO COMPLETO

### **🏗️ ESTRUCTURA DE RAMAS**
```
main (producción estable)
  ↑
release/* (próxima versión) 
  ↑  
feature/ALMA-* (desarrollo formal)
  ↑
dev/* (experimentación de ideas)
```

### **📋 RAMAS DEFINITIVAS**
```bash
main           # ✅ Producción estable
release/*      # ✅ Preparación para producción  
feature/ALMA-* # ✅ Desarrollo formal de funcionalidades
dev/*          # ✅ Experimentación y exploración de ideas
hotfix/ALMA-*  # ✅ Arreglos urgentes de producción
```

## 🔄 FLUJO COMPLETO PASO A PASO

### **1. 💡 NACE UNA IDEA NUEVA**
```bash
# Desde main
git checkout main
git pull origin main

# Crear rama de experimentación
git checkout -b dev/idea-autenticacion-biometrica

# Experimentar sin miedo
git add .
git commit -m "dev: explorar integración con sensor biométrico"
git commit -m "dev: probar diferentes flujos de autenticación"
```

### **2. 🎯 DECIDIR EL DESTINO DE LA IDEA**

#### **Opción A: La idea es BUENA y se implementa YA**
```bash
# Crear feature formal desde la dev
git checkout -b feature/ALMA-67-autenticacion-biometrica

# Limpiar historial de experimentación (opcional)
git reset --soft main
git commit -m "feat(auth): implementar autenticación biométrica"

# Continuar desarrollo formal
git add .
git commit -m "feat(auth): agregar validaciones de seguridad"
git commit -m "test(auth): agregar pruebas del sistema biométrico"
```

#### **Opción B: La idea es BUENA pero para MÁS ADELANTE**
```bash
# Guardar en main para referencia futura
git checkout main
git merge --no-ff dev/idea-autenticacion-biometrica
git commit -m "docs(ideas): archivar exploración de autenticación biométrica"
```

#### **Opción C: La idea NO FUNCIONA**
```bash
# Simplemente eliminar la rama
git branch -D dev/idea-autenticacion-biometrica
```

### **3. 🚀 DESARROLLO FORMAL DE FEATURE**
```bash
# Trabajar en la feature
git checkout feature/ALMA-67-autenticacion-biometrica

# Commits frecuentes y descriptivos
git add .
git commit -m "feat(auth): crear componente de captura biométrica"
git commit -m "feat(auth): integrar con backend de autenticación"
git commit -m "fix(auth): corregir error en validación de datos"
```

### **4. 📦 PREPARAR RELEASE**
```bash
# Crear rama de release desde main
git checkout main
git checkout -b release/v1.2.0

# Mergear feature completada
git merge --no-ff feature/ALMA-67-autenticacion-biometrica

# Testing final y ajustes
git commit -m "chore(release): ajustes finales v1.2.0"
```

### **5. 🏁 LANZAR A PRODUCCIÓN**
```bash
# Mergear a main
git checkout main
git merge --no-ff release/v1.2.0

# Taggear versión
git tag -a v1.2.0 -m "Versión 1.2.0 con autenticación biométrica"

# Eliminar ramas temporales
git branch -d release/v1.2.0
git branch -d feature/ALMA-67-autenticacion-biometrica
```

## 💾 ESTÁNDARES DE COMMITS

### **📝 COMMITS NORMALES (80% del tiempo)**
```bash
# ESTRUCTURA:
[tipo](ámbito): descripción breve (máx. 50 caracteres)

# EJEMPLOS:
feat(auth): agregar login con Google
fix(memory): resolver leak en procesamiento
docs(api): actualizar documentación
refactor(ui): simplificar componente
style(css): corregir indentación
test(login): agregar pruebas
chore(deps): actualizar React
```

### **🎯 TIPOS DE COMMITS**

| Tipo | Cuándo usarlo | Ejemplo |
|------|---------------|---------|
| `feat` | Nueva funcionalidad | `feat(search): agregar búsqueda` |
| `fix` | Corrección de bugs | `fix(crash): resolver error` |
| `docs` | Documentación | `docs(readme): agregar instrucciones` |
| `refactor` | Mejora código | `refactor(api): optimizar consultas` |
| `style` | Formato | `style(buttons): mejorar espaciado` |
| `test` | Pruebas | `test(login): agregar pruebas` |
| `chore` | Mantenimiento | `chore(build): actualizar webpack` |
| `dev` | Experimentación | `dev: explorar nueva tecnología` |

### **📖 COMMITS EXTENSOS (20% del tiempo)**
```bash
feat(payment): implementar sistema completo de pagos

- Integrar con Stripe para procesamiento
- Agregar formulario seguro
- Implementar manejo de errores
- Crear sistema de notificaciones

Archivos modificados:
• src/services/payment/
• src/components/PaymentForm/
• src/hooks/usePayment/

Resuelve: #ALMA-45
Depende de: #ALMA-32
```

## 🚨 GESTIÓN DE ERRORES

### **Corregir último commit:**
```bash
git add .
git commit --amend -m "feat(auth): crear componente corregido"
```

### **Deshacer cambios locales:**
```bash
# Archivo específico
git checkout -- archivo.html

# Todos los cambios
git reset --hard HEAD
```

### **Actualizar rama desactualizada:**
```bash
git checkout feature/mi-rama
git fetch origin
git merge origin/main
```

## 🎨 MANTENER GRAPH LIMPIO

### **Comando para visualizar:**
```bash
git log --oneline --graph --all --decorate -25
```

### **Resultado esperado:**
```
* a1b2c3d (feature/ALMA-67-auth) feat: implementar validaciones
* d4e5f6a feat: crear componente biometrico
| * 7g8h9i0 (dev/idea-auth) dev: explorar integración sensor
| * 1j2k3l4 dev: probar algoritmos
| * 5m6n7o8 dev: idea inicial
|/
* p9q0r1s (main) chore: actualizar dependencias
* t2u3v4w feat: sistema notificaciones v1.0
```

## 🚀 COMANDOS ESENCIALES

### **Estado y navegación:**
```bash
git status
git log --oneline -10
git branch -a
git checkout nombre-rama
```

### **Sincronización:**
```bash
git fetch --all
git pull origin main
git push origin nombre-rama
```

### **Guardado temporal:**
```bash
git stash
git stash list
git stash pop
```

### **Diferencias:**
```bash
git diff
git diff --staged
git diff HEAD~1
```

## 📋 REGLAS DE ORO

### **✅ HACER SIEMPRE:**
- [ ] Commits pequeños (máximo 5-10 archivos)
- [ ] Mensajes claros y específicos
- [ ] Trabajar en ramas feature/dev
- [ ] Actualizar main antes de empezar
- [ ] Usar `--no-ff` en merges importantes

### **❌ EVITAR SIEMPRE:**
- [ ] Commits con muchos cambios
- [ ] Trabajar directamente en main
- [ ] Mergear sin revisión
- [ ] Dejar ramas huérfanas

## 🎯 BENEFICIOS DE ESTE FLUJO

### **Para el desarrollador:**
- ✅ Espacio seguro para experimentar
- ✅ Historial claro y comprensible
- ✅ Menos presión al desarrollar
- ✅ Mejor organización de ideas

### **Para el proyecto:**
- ✅ Código production-ready en main
- ✅ Documentación automática del proceso
- ✅ Graph limpio y entendible
- ✅ Fácil seguimiento de features

---

## 📁 ¿DÓNDE GUARDAR ESTE ARCHIVO?

```bash
tu-proyecto/
├── GIT_STANDARDS.md    # ← Este archivo
├── README.md
├── src/
└── package.json
```

**¡Listo! Tienes un flujo completo que balancea experimentación con desarrollo formal, manteniendo un historial limpio y comprensible.**