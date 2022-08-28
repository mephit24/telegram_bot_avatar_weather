Bot edit your avatar in telegram account accordingly current weather.

Probably will be need install CairoSVG on your OS:

    for Linux https://www.cairographics.org/download/
    for Windows https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

For start:
1) Edit and rename .env.dist in app directory
2) Run once from app directory: python3 -m pip install -r requirements.txt
3) Run from app directory: python3 app.py

or

1) Execute: docker pull mephit/telegram_bot_avatar_weather:latest
2) Edit and rename /app/.env.dist inside container
3) Commit container
