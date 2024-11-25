# Groupe 24

Herald NKOUNKOU <herald.nkounkou@etu.univ-orleans.fr>
Thibault SO <thibault.so@etu.univ-orleans.fr>
Evan VILLAUME <evan.villaume@etu.univ-orleans.fr>
Amna MABROUK <amna.mabrouk@etu.univ-orleans.fr>

## Liste des Commandes

Ce fichier contient la liste des commandes utilisées pour traiter et répondre aux questions demandée.

1. **Créer un projet Django (Hérald)**  

   - Pour créer l’image Docker

      ```bash
         USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) USERID=$(id -u) docker-compose up -d
         docker exec -ti fw1-cc-herald
      ```

   - Dans django

      ```bash
         (django) [ herald | ~/workspace ] django-admin startproject cc
         (django) [ herald | ~/workspace ] cd cc
         (django) [ herald | ~/workspace/cc ] python manage.py startapp collec_management
         (django) [ herald | ~/workspace/cc ] python manage.py runserver 0.0.0.0:8088 &
      ```

2. **Créer une vue et un template (Hérald)**

   - Pour la creation des fichier qu'on aura besoin

      ```bash
        (django) [ herald | ~/workspace/cc ] cd collec_management
        (django) [ herald | ~/workspace/cc/collec_management ] mkdir templates
        (django) [ herald | ~/workspace/cc/collec_management ] touch urls.py
        (django) [ herald | ~/workspace/cc/collec_management ] cd templates
        (django) [ herald | ~/workspace/cc/collec_management/templates ] mkdir collec_management
        (django) [ herald | ~/workspace/cc/collec_management/templates/collec_management ] touch Presentation.html
      ```

   - On modifie ensuite les ficher cc/urls.py, collec_management/urls.py, /templates/collec_management/Presentation.html pour repondre a la questions

   ```text
      (django) [ herald | ~/workspace/cc ] python manage.py runserver 0.0.0.0:8088 &
      URL : http://localhost:8088/about/
   ```

3. **Créer un modèle Collec (Hérald)**

   - Aprés avoir modifier collec_management/models.py

   ```bash
      (django) [ herald | ~/workspace/cc ] python manage.py makemigrations
      (django) [ herald | ~/workspace/cc ] python manage.py migrate
      (django) [ herald | ~/workspace/cc ] python manage.py shell
   ```

   - Ensuite, dans le shell Python, exécutez les instructions suivantes pour Ajouter des données dans le modèle avec le shell Django

   ```shell
      from collec_management.models import Collec
      from django.utils import timezone
      collec = Collec.objects.create(
         title="Ma première collection",
         description="Description de la première collection",
         creation_date=timezone.now()
      )
      print(collec)
   ```

4. **Ajouter au moins douze collections différentes et réalistes (Hérald)**

   - on créé un scrip pour générer le JSON de maniere dynamique

   ```shell
         OUTPUT_FILE="fixtures/examples.json"
         # Par défaut, on génère 12 objets si aucun argument n'est fourni
         NUM_OBJECTS=${1:-12}

         mkdir -p fixtures #le -p pour si il existe deja

         # Début du contenu JSON
         echo "[" > $OUTPUT_FILE

         # Tableaux de mots pour créer des titres et descriptions aléatoires
         titles=("Collection" "Série" "Groupe" "Ensemble" "Lot")
         categories=("photographies" "peintures" "livres anciens" "vinyles" "timbres" "pièces de monnaie" "bandes dessinées" "cartes postales" "figurines" "montres" "sculptures" "cartes de jeu")
         descriptions=("Une collection de" "Un ensemble de" "Un groupe rare de" "Une série exclusive de" "Une belle sélection de")
         adjectives=("magnifiques" "anciennes" "modernes" "rares" "uniques" "classiques" "populaires" "exotiques")

         generate_random_date() {
            year=$(printf "%04d" $((RANDOM % 124 + 1900))) #une date entre 1900 et aujourdu'hui
            month=$(printf "%02d" $((RANDOM % 12 + 1)))
            day=$(printf "%02d" $((RANDOM % 28 + 1)))  # Limite à 28 jours pour éviter les probleme avec février 
            echo "$year-$month-$day"
         }

         # Boucle pour générer 12 collections avec des titres et descriptions aléatoires
         for ((i=0; i<$NUM_OBJECTS; i++)); do
            title="${titles[$RANDOM % ${#titles[@]}]} de ${categories[$i]}"
            description="${descriptions[$RANDOM % ${#descriptions[@]}]} ${adjectives[$RANDOM % ${#adjectives[@]}]} ${categories[$i]}."
            creation_date=$(generate_random_date)

            echo "    {" >> $OUTPUT_FILE
            echo "        \"model\": \"collec_management.collec\"," >> $OUTPUT_FILE
            echo "        \"pk\": $((i + 2))," >> $OUTPUT_FILE #le 1 est deja pris pour le test question 3
            echo "        \"fields\": {" >> $OUTPUT_FILE
            echo "            \"title\": \"$title\"," >> $OUTPUT_FILE
            echo "            \"description\": \"$description\"," >> $OUTPUT_FILE
            echo "            \"creation_date\": \"$creation_date\"" >> $OUTPUT_FILE
            echo "        }" >> $OUTPUT_FILE

            # Ajouter une virgule après chaque objet sauf le dernier
            if [ $i -lt $((NUM_OBJECTS - 1)) ]; then
               echo "    }," >> $OUTPUT_FILE
            else
               echo "    }" >> $OUTPUT_FILE
            fi
         done

         # Fin du contenu JSON
         echo "]" >> $OUTPUT_FILE

         echo "Le fichier fixtures/examples.json a été généré avec succès."
   ```

   - Ensuite ont l'utilise

   ```bash
      chmod +x questions4.sh

      cd collec_management
      ./questions4.sh 20 #avec le nombre de collec qu'on veux cree 12 par defaut ex ici 20
      cd ..
      python manage.py loaddata examples
   ```

5. **Détails d'une collection (Amna)**

   - Création du template 'collection_detail.html'

   ```bash
      (django) [ amna | ~/workspace/cc/collec_management/templates/collec_management ] touch collection_detail.html
      (django) [ amna | ~/workspace/cc/collec_management/templates/collec_management ] cd collection_detail.html   
   
   ```

   - Vérification du fonctionnement et test des fichier views.py, urls.py et collection_detail.html

   ```bash
      (django) [ amna | ~/workspace ] python manage.py runserver 0.0.0.0:8088 &

   ```

   - Commit lors de la fin du développement

   ```bash
      cc/collec_management/templates/collec_management/collection_detail.html$ git add .
      cc/collec_management/templates/collec_management/collection_detail.html$ git commit -m "<nom commit>"
   ```

6. **Liste des collections (Amna)**

   - Création du template 'collection_list.html'

   ```bash
      (django) [ amna | ~/workspace/cc/collec_management/templates/collec_management ] touch collection_list.html
      (django) [ amna | ~/workspace/cc/collec_management/templates/collec_management ] cd collection_list.html   
   
   ```

   - Vérification du fonctionnement et test des fichier views.py, urls.py et collection_list.html

   ```bash
      (django) [ amna | ~/workspace ] python manage.py runserver 0.0.0.0:8088 &

   ```

   - Commit lors de la fin du développement

   ```bash
      cc/collec_management/templates/collec_management/collection_list.html$ git add .
      cc/collec_management/templates/collec_management/collection_list.html$ git commit -m "<nom commit>"
   ```

7. **Ajout nouvelle collection (Evan)**

   - Création du template 'formulaire.html'

   ```bash
      (django) [ evan | ~/workspace/cc/collec_management/templates/collec_management ] touch formulaire.html
      (django) [ evan | ~/workspace/cc/collec_management/templates/collec_management ] cd formulaire.html   

   ```

   - Vérification du fonctionnement et test des fichier views.py, urls.py et formulaire.html

   ```bash
      (django) [ evan | ~/workspace ] python manage.py runserver 0.0.0.0:8088 &

   ```

   - Commit lors de la fin du développement

   ```bash
      cc/collec_management/templates/collec_management/formulaire.html$ git add .
      cc/collec_management/templates/collec_management/formulaire.html$ git commit -m "<nom commit>"
   ```

8. **Suppression d'une collection (Evan)**

   - Création du template 'delete_collection.html'

   ```bash
      (django) [ evan | ~/workspace/cc/collec_management/templates/collec_management ] touch delete_collection.html
      (django) [ evan | ~/workspace/cc/collec_management/templates/collec_management ] cd delete_collection.html   

   ```

   - Vérification du fonctionnement et test des fichier views.py, urls.py et formulaire.html

   ```bash
      (django) [ evan | ~/workspace ] python manage.py runserver 0.0.0.0:8088 &

   ```

   - Commit lors de la fin du développement

   ```bash
      cc/collec_management/templates/collec_management/delete_collection.html$ git add .
      cc/collec_management/templates/collec_management/delete_collection.html$ git commit -m "<nom commit>"
   ```

9. **Modification d'une collection (Thibault)**

   - Création du template 'modificationCollec.html'

   ```bash
      (django) [ thibault | ~/workspace/cc/collec_management/templates/collec_management ] touch modificationCollec.html
      (django) [ thibault | ~/workspace/cc/collec_management/templates/collec_management ] cd modificationCollec.html   
   
   ```

   - Vérification du fonctionnement et test des fichier views.py, urls.py et modificationCollec.html

   ```bash
      (django) [ thibault | ~/workspace ] python manage.py runserver 0.0.0.0:8088 &

   ```

   - Commit lors de la fin du développement

   ```bash
      cc/collec_management/templates/collec_management/modificationCollec.html$ git add .
      cc/collec_management/templates/collec_management/modificationCollec.html$ git commit -m "<nom commit>"
   ```

10. **Création de la page principale et menu (Thibault)**

      - Création du template 'main.html'

      ```bash
         (django) [ thibault | ~/workspace/cc/collec_management/templates/collec_management ] touch main.html
         (django) [ thibault | ~/workspace/cc/collec_management/templates/collec_management ] cd main.html   
      ```

      - Création du template 'Principal.html'

      ```bash
         (django) [ thibault | ~/workspace/cc/collec_management/templates/collec_management ] touch Principal.html
         (django) [ thibault | ~/workspace/cc/collec_management/templates/collec_management ] cd Principal.html   

      ```

      - Vérification du fonctionnement et test des fichier views.py, urls.py et Principal.html

      ```bash
         (django) [ thibault | ~/workspace ] python manage.py runserver 0.0.0.0:8088 &

      ```

      - Commit lors de la fin du développement

      ```bash
         cc/collec_management/templates/collec_management/Principal.html$ git add .
         cc/collec_management/templates/collec_management/Principal.html$ git commit -m "<nom commit>"
      ```

      Pour chaques questions traitée, une branche est crée

      ```bash
         cc/$ git checkout -b <nom de la branche>
      ```

      Une fusion est crée avec la branche créé et le master lors de la fin du développement

**Dernières Modifications**

   Après avoir fini le projet nous avons corrigé l'architecture pour qu'elle corresponde à celle attendue nous avons aussi ajouté dont le fichier .gitignore les derniers éléments.

   ```bash
      herald@MacBook-Air-de-HERALD fw1-cc1-24 % git tag Fin          
      herald@MacBook-Air-de-HERALD fw1-cc1-24 % git tag push Fin 
   ```
