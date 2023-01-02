mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
enableXsrfProtection=false\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml