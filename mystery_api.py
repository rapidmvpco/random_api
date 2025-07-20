from flask import Blueprint, Response

mystery_api_bp = Blueprint('mystery_api', __name__)

@mystery_api_bp.route('/mystery_api')
def home():
    html_content = """
    <html>
        <head>
            <title>Mystery Box API 🎁</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 2rem; background: #f5f5f5; }
                h1 { color: #6a0dad; }
                code { background: #eee; padding: 2px 6px; border-radius: 4px; }
                .box { background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
                a { color: #6a0dad; text-decoration: none; }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>🎁 Mystery Box API</h1>
                <p>Welcome to the Internet's most unpredictable API.</p>
                <p>Hit the endpoint <code>/mystery</code> to receive a completely random and potentially useless surprise.</p>
                <p>Example usage:</p>
                <ul>
                    <li><code>GET /mystery</code> → returns a random joke, fact, emoji combo, fake error, ASCII art, or other nonsense.</li>
                </ul>
                <p>This is a public API – no keys, no limits, just mystery.</p>
                <p>Made for fun. Enjoy the weirdness! 🌀</p>
                <hr>
                <p><a href="/mystery">Click here for a mystery</a></p>
            </div>
        </body>
    </html>
    """
    return Response(html_content, mimetype='text/html')
