# This script prints the list of words having phones with no maps to IITM phone set
# Call the script with the original lexicon as the first
# You can redirect it to a file list1 by using './phones_with_no_map.sh lexicon > list1'

# The phones without mapping are N, Th, t
touch counter
cut -f2- $1 | grep -nw N | cut -d':' -f1 > counter
cut -f2- $1 | grep -nw t | cut -d':' -f1 >> counter
cut -f2- $1 | grep -nw Th | cut -d':' -f1 >> counter


cat counter | while read line;do
sed "${line}q;d" $1
done
