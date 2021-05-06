# DeepCompose
Min repo för projektet DeepCompose.

## Vad?
DeepCompose är ett projekt vars mål är att skapa en AI som kan skapa musik likt Bach och andra kompositörer.

## Hur?
AIn använder GPT-2 modellen för att träna på alla Bachs verk, som scrapats från [BachCentral](http://www.bachcentral.com/midiindexcomplete.html), [piano-midi.de](http://www.piano-midi.de) samt [denna](https://www.youtube.com/watch?v=S6TVY6KGLW8) youtube video som midi filer och sedan omvandlat med *midi_to_txt.py* till en .txt fil, som GPT-2 gärna tränar på. Denna fil innehåller dock bara det första tracket och resterande tracks tas bort. Efter detta genererar den ett par verk, som man senare kan cleana och omvandla till .mid filer med *txt_to_midi.py*, och senare spela upp med valfri midi-spelare, exempelvis [denna](http://midiplayer.ehubsoft.net/).

Om man vill se hur träningen och genereringen ser ut kan man gå till [denna](https://colab.research.google.com/drive/1c3TKpM5sVTNjKenbBkkXnodo6GdYEOwG#scrollTo=N8KXuKWzQSsN) länk till Google Colab-en där allting sker. Detta verktyg är likt Jupyter Notebook men all kod körs på Googles datorer, så du kan använda din datorkraft för annat (exempelvis för att mina bitcoin). Källkoden för *midi_to_txt.py* och *txt_to_midi.py* kommer ifrån [MidiToText](https://github.com/dangeng/MidiToText) repon, och har modifierats lite för att anpassas för datans struktur och utdatans önskade struktur.

**OBS! Dessa script är skrivna i Python2, liksom några av de libraries som används av scripten. De kommer inte att fungera med Python3!**

## Varför?
Den huvudsakliga anledningen till att detta projekt körs är eftersom det tycks vara en kul och rolig grej, men det kan även tjäna ett lärande syfte och för att svara på frågor såsom *"Kan en AI skriva bra musik?"* och *"Är musik ett naturligt språk?"*.

## Struktur
I DeepCompose-mappen ligger all data och kod. Scripten *midi_to_txt.py* och *txt_to_midi.py* har ganska självförklarande syften, men i dessa finns kommentarer som visar var man måste ändra i koden för att anpassa till egna fil- och mappnamn beroende på var man har sina filer.

I *bach*-mappen ligger all data, som består av mappar med .mid filer med nästan alla Bachs verk (några var felaktigt formatterade och fungerade därför inte med *midi_to_txt.py*). Här ligger även de två andra dataset som använts.

I *texts*-mappen ligger alla .txt filer i folders beroende på vilket dataset som använts. I 5000-mappen ligger det som genererats för midiclassics-datasetet fast som tränats 10 ggr. längre.

I *generated*- mappen ligger alla .mid filer som konverterats från .txt filer i *texts*-mappen.

Scriptet *unpack.py* användes för att fixa strukturen för *midiclassics* datasetet genom att flytta ut filerna från sub-directories inuti varje kompositörs egna folder.

I Google Colab-en finns koden som tränar AIn, kod för att generera texterna samt vikterna.
