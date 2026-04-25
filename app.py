"""
Главный файл запуска Dash-приложения.
"""
import dash
import dash_bootstrap_components as dbc

from layout import create_layout
from callbacks_curve import register_callbacks as register_curve
from callbacks_points import register_callbacks as register_points
from callbacks_bonds import register_callbacks as register_bonds
from callbacks_utils import register_callbacks as register_utils

# Создаём экземпляр приложения с подавлением исключений для несуществующих компонентов
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title='ZCYC',
    suppress_callback_exceptions=True   # <-- добавляем эту строку
)

server = app.server

# Устанавливаем макет
app.layout = create_layout()

# Регистрируем все колбэки
register_curve(app)
register_points(app)
register_bonds(app)
register_utils(app)

if __name__ == '__main__':
    print("Запуск ZCYC Dashboard...")
    print("Откройте браузер и перейдите по адресу: http://localhost:8888")
    app.run(debug=True, host='0.0.0.0', port=8888)