# Telegram Bot

```bash
pre-commit run --all-files && git status && \
echo -n "Confirm update and commit by enter \"y/n\": " && \
read ans && echo "$ans" | grep -iq "y" && git add --all && \
git status && cz c && git push || echo "Exit"
```

```bash
git push -f --set-upstream origin main
```

## Build docker image

```bash
docker-compose -f docker-compose.yml build && docker-compose up
```
