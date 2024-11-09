# Trading Bot with Reinforcement Learning (RL)

## Project Description
Dette prosjektet bruker **Reinforcement Learning** (RL) med **PPO (Proximal Policy Optimization)** for å bygge en AI som kan handle aksjer basert på historiske data. GUI-et gir brukeren muligheten til å starte tradingboten og koble til en exchange med API-nøkler.

## how to start

1. Installer nødvendige biblioteker:


2. Legg til ditt egne API-nøkler i GUI-en.

3. Last ned aksjeprisdata (historiske data) som CSV-fil og plasser det i `data/stock_data.csv`.

4. Kjør hovedfilen:



## how to trainmodel
- Du kan trene RL-modellen med et aksjepris-datasett ved å bruke `bot/model.py`. Modellen lagres som en `.zip`-fil.
