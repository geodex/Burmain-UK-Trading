#Prompt: Thought for 31s

Build a Django backend for a fully functional trading platform web application, integrated with Interactive Brokers (IB) TWS API as the primary broker, and modular support for additional brokers like KuCoin, Exness, and eToro. The backend should use Django 4.x with REST Framework for APIs, Channels for WebSockets, Celery for background tasks, and Redis for caching. Structure the project with apps for auth, trading, admin_panel, brokers, and payments. Use MariaDB as the database via Django ORM.

Key backend components and requirements:

    Project Structure: Create a Django project named 'trading_platform' with apps: 'users' (for auth and profiles), 'trading' (for orders, portfolios, quotes), 'brokers' (modular integrations), 'payments' (deposits/withdrawals), 'news' (feeds), 'admin_panel' (custom admin views). Include a 'core' app for shared utilities.
    Settings (settings.py): Configure for production-ready setup: SECRET_KEY from env, DEBUG=False for prod, ALLOWED_HOSTS=['*'], INSTALLED_APPS including django.contrib.admin, rest_framework, channels, celery, etc. Database: ENGINE='django.db.backends.mysql', NAME='trading_db', USER='root', PASSWORD from env, HOST='db' (for Docker). Middleware for security (CSRF, XSS). ASGI_APPLICATION for Channels. CELERY_BROKER_URL='redis://redis:6379/0'. STATIC/MEDIA files setup. REST_FRAMEWORK with JWT auth (using simple_jwt). Email backend for notifications.
    Models (in respective apps):
        Users: Custom User model extending AbstractUser with fields like email (unique), phone, is_verified, kyc_status (choices: pending, approved, rejected), balance (DecimalField), preferences (JSONField for alerts, themes).
        Brokers: Broker model (name, api_key, api_secret, per user), UserBrokerConfig (links user to broker with credentials).
        Trading: Order (user, broker, symbol, type, quantity, price, status), Position (user, broker, symbol, quantity, entry_price), Portfolio (aggregated views via managers), Watchlist (user, symbols).
        Payments: Deposit/Withdrawal (user, amount, method: manual/stripe, status, transaction_id).
        News: Article (title, content, source, date).
        KYC: Document (user, type: id/passport, file, status).
    Views and APIs (using DRF ViewSets):
        Auth: Registration (email verification via token), Login (JWT), Profile update, 2FA setup/verification (using pyotp for Authy-like).
        Trading: Endpoints for quotes (real-time via WebSockets), order placement (async with ib_insync), portfolio overview (aggregate across brokers), risk calc (VaR using numpy/scipy if needed).
        Admin: Custom views for user management, API key gen/revoke, system settings, KYC review (manual upload, Onfido API hook: use onfido-python lib for check initiation).
        Payments: Stripe integration (webhooks for charges), manual approval views.
        News: CRUD for admins, RSS fetch background task (using feedparser).
    Broker Integrations (in brokers app): Abstract base class BrokerAdapter with methods: connect, get_quote, place_order, get_positions, etc. Implement IBAdapter (using ib_insync.asyncio), KuCoinAdapter (kucoin-python or ccxt), ExnessAdapter (mt5lib if available), eToroAdapter (if API allows). Use env vars for credentials. Handle paper trading modes.
    WebSockets (consumers.py): Using Django Channels for live updates: QuoteConsumer (subscribe to symbols, push via broker feeds), NotificationConsumer (order status, alerts).
    Tasks (celery.py): Background jobs for email/SMS (django-celery-email, Twilio lib), news fetching, trade processing, push notifications (firebase-admin).
    Security: Use argon2 for hashing (django-argon2), rate limiting (django-ratelimit), audit logs (django-simple-history). KYC hooks: Manual file uploads, Onfido integration for automated checks.
    Utils: Fee calculator, multi-currency converter (using rates from brokers), error handlers for broker failovers.
    Tests: Include pytest setups for models, views, integrations (mock brokers with unittest.mock).

Generate the complete code for the backend, starting with the main 'manage.py' and 'wsgi.py'/'asgi.py', then settings.py, urls.py, and app-specific files (models.py, views.py, serializers.py, consumers.py, tasks.py). Use placeholders for env vars (e.g., os.environ.get('IB_API_KEY')). Ensure it's deployable to Apache with mod_wsgi, and compatible with Docker/MariaDB/Redis.
