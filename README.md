# PathSearchReplacer
Replace one word with another in all files of a directory and all subdirectories.
# Warning
Be carefuly with this script, you could accidentaly modify several files that would change the well working of your machine.

# Parameters
## directory (Type:String)
This is the directory where the script will begin to search any coincidence to modify the files and subdirectories.

## Extensions (Type:array)
An array of the extensions that will be searched. (Leave Empty to search in any file.)
## Word_by_search 
This is the word that will be search and then replaced
## Word_by_replace 
This is the word that will be replaced

# Considerations
This script will change the word, even if the word is inside another sentence. For example:

|   string        | Word Searched | Word to replace |     Result   |
|-----------------|:-------------:|:---------------:|-------------:|
| **xtml**        |    xtml       |       XYZ       | **XYZ**      |
| abc**xtml**     |    xtml       |       XYZ       | abc**XYZ**   |
| abc**xtml**def  |    xtml       |       XYZ       | abc**XYZ**def|
