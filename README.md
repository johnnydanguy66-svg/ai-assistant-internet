# 🤖 AI Assistant Connecté à Internet

Une intelligence artificielle fonctionnelle et simple à utiliser, avec accès à Internet en temps réel.

## 🚀 Démarrage Rapide

### Étape 1: Obtenir une Clé API Gratuite
1. Allez sur: https://makersuite.google.com/app/apikey
2. Cliquez sur "Create API Key"
3. Copié votre clé API

### Étape 2: Installer Python
- **Windows/Mac/Linux**: Téléchargez Python 3.8+ depuis https://python.org

### Étape 3: Configuration
1. Ouvrez le fichier `ai_assistant.py` dans un éditeur de texte
2. Cherchez la ligne: `API_KEY = "votre_cle_api_google_gemini_ici"`
3. Remplacez par votre vraie clé API:
```python
API_KEY = "AIzaSyD_votre_cle_api_ici"
```

### Étape 4: Exécution
```bash
python ai_assistant.py
```

## 💡 Utilisation

### Questions Normales
```
👤 Vous: Qu'est-ce que Python?
🤖 IA: Python est un langage de programmation...
```

### Recherche Internet
```
👤 Vous: internet: actualités technologie 2026
🔍 Recherche sur Internet: actualités technologie 2026
📰 Résultat trouvé: ...
```

### Commandes
- `aide` - Afficher l'aide
- `quitter` ou `exit` - Quitter
- `internet: <votre_recherche>` - Rechercher sur Internet

## 📋 Fonctionnalités

✅ **IA Générative** - Réponses intelligentes et contextuelles  
✅ **Accès Internet** - Recherche en temps réel  
✅ **Gratuit** - Utilise l'API gratuite de Google Gemini  
✅ **Portable** - Copiez-collez le code n'importe où  
✅ **Interface Simple** - Facile à utiliser  

## 🔧 Dépendances Installées Automatiquement

- `google-generativeai` - IA Google Gemini
- `requests` - Requêtes HTTP

## ⚙️ Configuration Avancée

### Modifier le Modèle IA
Dans `ai_assistant.py`, ligne 62:
```python
model = genai.GenerativeModel('gemini-pro')  # Changez le modèle
```

### Ajouter d'autres Sources de Recherche
Modifiez la fonction `rechercher_internet()` pour utiliser:
- Google Search API
- Wikipedia API
- NewsAPI
- Autres APIs

## 🐛 Dépannage

### "ModuleNotFoundError: No module named 'google'"
```bash
pip install google-generativeai requests
```

### "API Key not valid"
Vérifiez votre clé API sur https://makersuite.google.com/app/apikey

### "No internet connection"
Vérifiez votre connexion Internet

## 📝 Exemple Complet

```
🤖 AI ASSISTANT CONNECTÉ À INTERNET 🤖
==================================================

✅ IA initialisée avec succès!

📖 COMMANDES:
  - 'internet: <requete>' - Rechercher sur Internet
  - 'quitter' ou 'exit' - Quitter l'application
  - 'aide' - Afficher cette aide

👤 Vous: Quelle est la capitale de la France?
🤖 IA: La capitale de la France est Paris, la plus grande ville du pays...

👤 Vous: internet: météo Paris aujourd'hui
🔍 Recherche sur Internet: météo Paris aujourd'hui
📰 Résultat trouvé: La météo à Paris aujourd'hui est...

👤 Vous: quitter
👋 Au revoir!
```

## 🎓 Améliorations Possibles

- [ ] Ajouter une base de données pour l'historique
- [ ] Interface graphique (GUI avec Tkinter)
- [ ] Support multi-langue
- [ ] Intégration avec plus de sources Internet
- [ ] Sauvegarde des conversations
- [ ] Mode voix (Text-to-Speech)

## 📄 Licence

MIT License - Libre d'utilisation

## 🤝 Support

Besoin d'aide? Consultez:
- Documentation Google Gemini: https://ai.google.dev/
- Forum Python: https://www.python.org/community/

---

**Créé avec ❤️ pour les développeurs**
