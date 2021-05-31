# Converts lexicon to IITM challenge format using mappings as discussed
lexicon=$1
new_lexicon=$2

sed 's/\baa\b/a/g' $lexicon > $new_lexicon

sed -i 's/\bAA\b/aa/g' $new_lexicon

sed -i 's/\bae\b/ei/g' $new_lexicon

sed -i 's/\baw\b/aa uu/g' $new_lexicon

sed -i 's/\bay\b/aa y/g' $new_lexicon

sed -i 's/\bD\b/dx/g' $new_lexicon

sed -i 's/\bDh\b/dxh/g' $new_lexicon

sed -i 's/\bex\b/ee/g' $new_lexicon

sed -i 's/\bhh\b/h/g' $new_lexicon

sed -i 's/\bii\b/i/g' $new_lexicon # must do this before next sed

sed -i 's/\bII\b/ii/g' $new_lexicon # must do this after prev sed

sed -i 's/\bN\b/nx/g' $new_lexicon

sed -i 's/\boo\b/o/g' $new_lexicon

sed -i 's/\bOO\b/ou/g' $new_lexicon

sed -i 's/\boy\b/ou y/g' $new_lexicon

sed -i 's/\bT\b/tx/g' $new_lexicon

sed -i 's/\bTh\b/txh/g' $new_lexicon

sed -i 's/\buu\b/u/g' $new_lexicon

sed -i 's/\bUU\b/uu/g' $new_lexicon

sed -i 's/\bzh\b/jh/g' $new_lexicon

wait

python3 lexicon_mapper_nodict.py $new_lexicon > tmp
cat $new_lexicon tmp > ${new_lexicon}_iitm.txt
sed -i 's/  / /g' ${new_lexicon}_iitm.txt
sed -i 's/  / /g' ${new_lexicon}_iitm.txt
rm $new_lexicon
