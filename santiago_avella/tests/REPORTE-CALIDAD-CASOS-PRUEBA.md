# Documentación de Casos de Prueba y Reporte de Calidad

## Dominio: Psicología (Entidad: consulta)

### Resumen
Suite de pruebas automatizadas para la gestión de consultas psicológicas. Incluye casos de éxito, error y validaciones de lógica de negocio.

## Casos de Prueba Implementados
- Crear consulta válida
- Crear consulta con campo faltante
- Obtener consulta por ID
- Consulta no encontrada
- Actualizar consulta existente
- Eliminar consulta
- Actualizar campo inválido
- Listar todas las consultas

## Cobertura y Calidad
- Cobertura esperada: >80%
- Validaciones de campos, errores y lógica de negocio

## Ejecución
pytest --cov=main

---
Autor: Santiago Avella
Ficha: 3147247
Fecha: 28/09/2025
