## 🌿 Flujo de trabajo con Ramas (Branches)

Trabajar en ramas te permite desarrollar nuevas funciones de forma segura sin afectar el proyecto principal. Sigue estos pasos para crear, usar y subir tu rama a GitHub:

```bash
# 1. Crear una nueva rama
git branch <nombre-de-tu-rama>

# 2. Moverte a la rama que acabas de crear
git switch <nombre-de-tu-rama>

# 💡 ATAJO: Crear y moverte a la rama en un solo paso
git switch -c <nombre-de-tu-rama>

# 3. Trabaja en tus archivos y guarda los cambios localmente
git add .
git commit -m "Descripción breve de lo que hiciste"

# 4. Subir la rama nueva a GitHub por primera vez
git push -u origin <nombre-de-tu-rama>
