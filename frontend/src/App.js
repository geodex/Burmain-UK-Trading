#Prompt: Build a React frontend for a fully functional trading platform web application, using React 18.x with Material-UI (MUI) 5.x for styling, React Router 6.x for navigation, and Axios for API calls to the Django backend. The UI should be modern, responsive, and intuitive like Robinhood, with minimal clicks for key actions (e.g., one-tap buys/sells, swipeable charts). Incorporate theme switching (light/dark modes) using MUI's ThemeProvider and localStorage for persistence. Use a trust-inspiring color palette: primary blue (#007BFF) for actions, accent green (#28A745) for positives (gains, buys), neutral grays (#F8F9FA backgrounds, #6C757D text), with subtle gradients/shadows for a flat, professional design.
Key frontend components and requirements:

Project Structure: Assume folders like src/components (for reusable like Navbar, Footer, Chart, OrderForm), src/pages (Landing, Dashboard, Portfolio, Trading, News, Profile, AdminDashboard), src/context (AuthContext, ThemeContext, BrokerContext), src/services (API calls, WebSocket hooks), src/utils (helpers like feeCalculator).
App.js Setup:

Imports: React, useState/useEffect, ThemeProvider/createTheme from @mui/material, Router/BrowserRouter/Routes/Route from react-router-dom, CssBaseline, axios, socket.io-client or channels for WebSockets.
Theme: Create light/dark themes with MUI's createTheme, using the specified palette. Use a ThemeContext Provider for toggling (default light, persist in localStorage).
Routing: Protected routes for auth (e.g., PrivateRoute component checking JWT in localStorage). Routes: '/' (LandingPage), '/login', '/register', '/dashboard' (user dashboard with portfolio, watchlists), '/trade/:symbol' (trading page with quotes/charts/orders), '/news', '/profile' (edit details, KYC upload), '/admin' (admin panel with user management, settings, API keys).
Providers: Wrap app in AuthProvider (manages JWT, user data from backend), BrokerProvider (handles multi-broker selection), NotificationProvider (for toasts/alerts via notistack or MUI Snackbar).
WebSockets: Use useEffect to connect to Django Channels (e.g., via websocket-bridge or socket.io if adapted) for real-time quotes/notifications. Integrate with backend consumers.
Global Styles: CssBaseline, custom typography (e.g., Roboto font), responsive breakpoints.
Error Handling: Global error boundary, loading spinners (MUI CircularProgress).


Main Components (briefly describe for generation):

LandingPage: Hero with benefits, sign-up form, news ticker (fetch from backend), testimonials.
Dashboard: Portfolio overview (charts with Recharts or TradingView embed), aggregated P&L across brokers, recent trades, gamified badges.
Trading Page: Real-time quotes (WebSocket updates), order form (one-tap buy/sell), watchlist, risk calculator.
AdminDashboard: Tabs for users, settings, KYC reviews (manual/Onfido status), API key management.
News: Feed with cards, comments section.
Profile: Form for updates, deposit/withdrawal (Stripe integration via react-stripe-js), 2FA setup.


Integrations:

API Calls: Axios interceptors for JWT auth, baseURL from env (e.g., '/api'). Endpoints for auth, trading, payments.
Real-Time: WebSocket hooks for live data; push notifications via Firebase (use @firebase/messaging).
Charts: Integrate Chart.js or TradingView for symbols.
Security: Input validation, CSRF via backend tokens.
Accessibility: ARIA labels, keyboard nav in MUI components.
Simplicity: Mobile-first, swipe gestures (react-swipeable), minimal UI clutter.


Deployment Notes: Ensure buildable with 'npm run build' for static serving via Apache in production.

Generate the complete code for App.js, including all imports, theme creation, context providers, routing setup, and the main return JSX. Use functional components with hooks. Add comments for clarity. Assume other components are imported (e.g., import LandingPage from './pages/LandingPage'). Use env vars for API_URL, etc. (process.env.REACT_APP_API_URL).
