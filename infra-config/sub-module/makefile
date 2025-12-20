.PHONY: typing typing-test typing-summary clean

# Vérification stricte avec mypy
typing:
	mypy --config-file mypy.ini --show-error-codes --pretty .

# Vérification avec capture des logs et résumé compact
typing-test:
	@mkdir -p artifacts/typing
	@mypy --config-file mypy.ini --show-error-codes --pretty . \
		--log-file artifacts/typing/mypy.log || true
	@echo "=== Résumé des 200 dernières lignes ==="
	@tail -n 200 artifacts/typing/mypy.log || true

# Génère un résumé statistique par code d'erreur
typing-summary:
	@mkdir -p artifacts/typing
	@grep -oE '\[[a-z0-9-]+\]' artifacts/typing/mypy.log | sort | uniq -c | sort -nr || true

# Nettoyage des artefacts
clean:
	@rm -rf artifacts/typing