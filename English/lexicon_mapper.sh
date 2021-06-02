# Converts lexicon to IITM English challenge format using mappings as discussed
# Run as ./lexicon_mapper.sh global_lexicon.txt global_lexicon_new to convert the global_lexicon.txt input to global_lexicon_new with english IITM phone set
lexicon=$1
new_lexicon=$2

sed 's/\baa\b/AH/g' $lexicon > $new_lexicon

sed -i 's/\bAA\b/AA/g' $new_lexicon

sed -i 's/\bae\b/AE/g' $new_lexicon

sed -i 's/\baw\b/AW/g' $new_lexicon

sed -i 's/\bay\b/AY/g' $new_lexicon

sed -i 's/\bb\b/B/g' $new_lexicon
sed -i 's/\bbh\b/B HH/g' $new_lexicon

sed -i 's/\bc\b/CH/g' $new_lexicon
sed -i 's/\bch\b/CH HH/g' $new_lexicon

sed -i 's/\bd\b/DH/g' $new_lexicon
sed -i 's/\bdh\b/DH HH/g' $new_lexicon

sed -i 's/\bD\b/D/g' $new_lexicon

sed -i 's/\bDh\b/D HH/g' $new_lexicon

sed -i 's/\bee\b/EY/g' $new_lexicon #> ${new_lexicon}_alt
#sed -i 's/\bee\b/AH IH/g' $new_lexicon

#cat $new_lexicon ${new_lexicon}_alt | sort -u > tmp
#mv tmp $new_lexicon

sed -i 's/\bex\b/EH/g' $new_lexicon

sed -i 's/\bf\b/F/g' $new_lexicon

sed -i 's/\bg\b/G/g' $new_lexicon

sed -i 's/\bgh\b/G HH/g' $new_lexicon

sed -i 's/\bhh\b/HH/g' $new_lexicon

sed -i 's/\bii\b/IH/g' $new_lexicon

sed -i 's/\bII\b/IY/g' $new_lexicon

sed -i 's/\bj\b/JH/g' $new_lexicon

sed -i 's/\bjh\b/JH HH/g' $new_lexicon

sed -i 's/\bk\b/K/g' $new_lexicon

sed -i 's/\bkh\b/K HH/g' $new_lexicon

sed -i 's/\bl\b/L/g' $new_lexicon

sed -i 's/\bm\b/M/g' $new_lexicon

sed -i 's/\bN\b/N/g' $new_lexicon

sed -i 's/\bn\b/N/g' $new_lexicon

sed -i 's/\boo\b/OW/g' $new_lexicon

sed -i 's/\bOO\b/AO/g' $new_lexicon

sed -i 's/\boy\b/OY/g' $new_lexicon

sed -i 's/\bp\b/P/g' $new_lexicon
sed -i 's/\bph\b/P HH/g' $new_lexicon

sed -i 's/\br\b/R/g' $new_lexicon

sed -i 's/\bs\b/S/g' $new_lexicon

sed -i 's/\bsh\b/SH/g' $new_lexicon

sed -i 's/\bt\b/TH/g' $new_lexicon

sed -i 's/\bT\b/T/g' $new_lexicon

#sed 's/\bth\b/T HH/g' $new_lexicon > ${new_lexicon}_alt
sed -i 's/\bth\b/TH/g' $new_lexicon

#cat $new_lexicon ${new_lexicon}_alt | sort -u > tmp
#mv tmp $new_lexicon

sed -i 's/\bTh\b/T HH/g' $new_lexicon

sed -i 's/\buu\b/UH/g' $new_lexicon

sed -i 's/\bUU\b/UW/g' $new_lexicon

sed -i 's/\bw\b/W/g' $new_lexicon

sed -i 's/\by\b/Y/g' $new_lexicon

sed -i 's/\bz\b/Z/g' $new_lexicon

sed -i 's/\bzh\b/ZH/g' $new_lexicon

wait
#rm ${new_lexicon}_alt

