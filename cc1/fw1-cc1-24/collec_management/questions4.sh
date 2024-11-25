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

echo "Le fichier fixtures/examples.json a été généré avec succès"


