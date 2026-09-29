#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Assistant Connecté à Internet
Copiez ce code dans un fichier .py et exécutez-le
"""

import os
import sys
import requests
from datetime import datetime

try:
    import google.generativeai as genai
except ImportError:
    print("Installation des dépendances requises...")
    os.system("pip install google-generativeai requests")
    import google.generativeai as genai

# Configuration - Remplacez par votre clé API Google Gemini
API_KEY = "votre_cle_api_google_gemini_ici"

def configurer_ia():
    """Configure l'IA avec votre clé API"""
    if API_KEY == "votre_cle_api_google_gemini_ici":
        print("⚠️  ATTENTION: Vous devez ajouter votre clé API Google Gemini!")
        print("Obtenez une clé gratuite sur: https://makersuite.google.com/app/apikey")
        return False
    
    genai.configure(api_key=API_KEY)
    return True

def rechercher_internet(requete):
    """Recherche sur Internet"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        url = f"https://api.duckduckgo.com/?q={requete}&format=json"
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Erreur de recherche: {e}")
        return None

def obtenir_contexte_internet(requete):
    """Obtient des informations d'Internet pour améliorer les réponses"""
    try:
        results = rechercher_internet(requete)
        if results and 'AbstractText' in results:
            return results['AbstractText']
        return ""
    except:
        return ""

def generer_reponse_ia(prompt, contexte_internet=""):
    """Génère une réponse avec l'IA"""
    try:
        model = genai.GenerativeModel('gemini-pro')
        
        # Combine le prompt avec le contexte internet
        prompt_enrichi = f"""{prompt}

Contexte Internet actuel (si applicable): {contexte_internet}

Répondez de manière détaillée et utile. Utilisez le contexte internet pour fournir des informations actuelles."""
        
        response = model.generate_content(prompt_enrichi)
        return response.text
    except Exception as e:
        return f"Erreur IA: {str(e)}"

def afficher_titre():
    """Affiche le titre de l'application"""
    print("\n" + "="*50)
    print("🤖 AI ASSISTANT CONNECTÉ À INTERNET 🤖")
    print("="*50)
    print(f"Heure: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("="*50 + "\n")

def afficher_aide():
    """Affiche l'aide"""
    print("\n📖 COMMANDES:")
    print("  - 'internet: <requete>' - Rechercher sur Internet")
    print("  - 'quitter' ou 'exit' - Quitter l'application")
    print("  - 'aide' - Afficher cette aide\n")

def main():
    """Fonction principale"""
    afficher_titre()
    
    # Vérifier la configuration
    if not configurer_ia():
        sys.exit(1)
    
    print("✅ IA initialisée avec succès!")
    afficher_aide()
    
    while True:
        try:
            # Entrée utilisateur
            utilisateur_input = input("👤 Vous: ").strip()
            
            if not utilisateur_input:
                continue
            
            # Commandes spéciales
            if utilisateur_input.lower() in ['quitter', 'exit', 'q']:
                print("\n👋 Au revoir!")
                break
            
            if utilisateur_input.lower() == 'aide':
                afficher_aide()
                continue
            
            # Recherche Internet
            if utilisateur_input.lower().startswith('internet:'):
                requete = utilisateur_input[9:].strip()
                print(f"\n🔍 Recherche sur Internet: {requete}")
                contexte = obtenir_contexte_internet(requete)
                if contexte:
                    print(f"📰 Résultat trouvé: {contexte}\n")
                else:
                    print("❌ Aucun résultat trouvé\n")
                continue
            
            # Traitement IA normal
            print("\n🤖 IA: ", end="", flush=True)
            
            # Essayer d'obtenir un contexte internet pertinent
            contexte = obtenir_contexte_internet(utilisateur_input[:50])
            
            reponse = generer_reponse_ia(utilisateur_input, contexte)
            print(reponse)
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Interruption... Au revoir!")
            break
        except Exception as e:
            print(f"❌ Erreur: {e}\n")

if __name__ == "__main__":
    main()
