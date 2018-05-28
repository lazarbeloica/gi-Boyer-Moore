# gi-Boyer-Moore
School project for Genome Informatics course

# Course information
Assignment list:
https://docs.google.com/document/d/1XqrPYwFnEYNOKzHntZQfz1L8b59BN8WIVvNgDyIUE0I/edit#heading=h.i7nzefwji0hn

Course sources:
https://github.com/vladimirkovacevic/comp_gen

# Assignment
The text of the assignment is the following (in Serbian):

Boyer-Moore algoritam koristi heuristike (Bad character and Good suffix rule) za preskakanje nepotrebnih poređenjakaraktera pri pretraživanju. Definisati na sličan način dve heuristike (heuristika 1 i heuristika 2) koje mogu bitiprimenjivane za sračunavanje maksimalno dozvoljenog pomeraja. Za formiranje heuristika koristiti samo patern -algoritam treba da ostane on-line (10 poena).

Izvršiti merenje i poređenje vremena izvršavanja i memorijskog zauzeća seta on-line Exact Matching algoritama:

* Boyer-Moore - Heuristika 1 + Heuristika 2
* Boyer-Moore - Heuristika 1
* Boyer-Moore - Heuristika 2
* Boyer-Moore - Strong good suffix rule and bad character rule

Napisati wrapper funkciju ili klasu u programskom jeziku Python koja ima mogućnost izvršavanja zadate varijante algoritma na osnovu ulaznog parametra. Kao test podatke koristiti 3 seta podataka (5 poena):

* Tekst: Canis lupus familiaris genom, Chromosome 1 i paterni: ATGATG, CTCTCTA, TCACTACTCTCA
* Tekst: Phoenix dactylifera genome, i paterni: ATGATG, CTCTCTA, TCACTACTCTCA

Genom po slobodnom izboru iz NIH baze i proizvoljna 3 paterna različite dužine.

Dobijene rezultate predstaviti tabelarno i grafički (Python matplotlib). Grafički način (dijagram) treba da bude dovoljno intuitivan da onaj koji ga čita može brzo izvući potrebne zaključke vezane za performanse zadatih varijanti algoritama (5 poena).

Za svaku od funkcija u kodu napisati testove (5 poena).
Pripremiti prezentaciju (Google slides ili power point) algoritama koji se testiraju, kao i samih rezultata (5 poena).
Pripremiti video prezentaciju projekta (3 - 5 minuta trajanja) koja će biti dostupna na YouTube ili drugom video servisu na kojem mu je moguće pristupiti (10 poena).

Zadatak je predviđen za dva studenta.

# Running

The program entrance point is located in src/main.py

It is necessary to specify the list of heuristics to use by specifying a '-h' flag and after that a list of heuristics should be given. The list elements should be separated with a ' '.
The possible heuristics are:
* bc - BadCharacter
* gs - GoodSuffix
* fh - FirstHeuristic aka Boyer-Moore-Horesepool
* sh - SecondHeuristic aka Imporived-Boyer-Moore-Horesepool-Sunday

It is possible to give a composite heuristic to use by using a '+' between heuristics.
Ex: bc+gs+fh - this will produce a composite of BadCharacter, GoodSufix and FirstHeuristc to be used

It is necessary to specify a list of "file pattern" pairs to be used for the algorithm. This is done by giving a
'-c' flag and a "file pattern" list that follows. The list elements should be separated with a ' '.

Ex: ptyhom src/main.py -h fh+sh fh sh bc+gs -c C:\Canis_lupus_chr_1 ATGATG C:\Canis_lupus_chr_1 CTCTCTA C:\Canis_lupus_chr_1 TCACTACTCTCA C:\Phoenix_dactylifera_gen ATGATG

Note: Every given heuristic will be run against every given file.

# Running Tests

It is possible to run all unit and integration tests (around 100 tests) by executing a make test command.
If you wish to run a particular test, they can be found in the src/tests dir.

# More information

A video presentation is available on https://www.youtube.com/watch?v=hDWtuRIGoPs&feature=youtu.be
This presentation is also available as pdf and it is located in docs dir.

The code itself is documented and can be found in the src folder.
