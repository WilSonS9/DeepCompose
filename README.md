# DeepCompose
Min repo för projektet DeepCompose.

## Vad?
DeepCompose är ett projekt vars mål är att skapa ett AI som kan skapa musik likt Bach och andra kompositörer.

## Hur?
AIn använder GPT-2 modellen för att träna på alla Bachs verk, som scrapats från http://www.bachcentral.com/midiindexcomplete.html som midi och sedan omvandlat med *midi_to_txt.py* till en .txt fil, som GPT-2 gärna tränar på. Denna fil innehåller dock bara det första tracket och resterande tracks tas bort. Efter detta genererar den ett par verk, som man senare kan cleana och omvandla till .mid filer med *txt_to_midi.py*, och senare spela upp med valfri midi-spelare, exempelvis [denna](http://midiplayer.ehubsoft.net/).

Om man vill se hur träningen och genereringen ser ut kan man gå till [denna](https://colab.research.google.com/drive/1c3TKpM5sVTNjKenbBkkXnodo6GdYEOwG#scrollTo=N8KXuKWzQSsN) länk till Google Colab-en där allting sker. Detta verktyg är likt Jupyter Notebook men all kod körs på Googles datorer, så du kan använda din datorkraft för annat (exempelvis för att mina bitcoin). Källkoden för *midi_to_txt.py* och *txt_to_midi.py* kommer ifrån [MidiToText](https://github.com/dangeng/MidiToText) repon, och har modifierats lite för att anpassas för datans struktur och utdatans önskade struktur.

**OBS! Dessa script är skrivna i Python2, liksom några av de libraries som används av scripten. De kommer inte att fungera med Python3!**

## Varför?
Den huvudsakliga anledningen till att detta projekt körs är eftersom det tycks vara en kul och rolig grej, men det kan även tjäna ett lärande syfte och för att svara på frågor såsom *"Kan ett AI skriva bra musik?"* och *"Är musik ett naturligt språk?"*.
