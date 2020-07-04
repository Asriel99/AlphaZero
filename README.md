 This is a beta implementation based in another code just for learning, in font has to tic tac toe ( jogo da velha), Othello, Connect Four but last 2 games is not implemented here;


Games implemented:
1) Tic Tac Toe

Games implemented in futures versions 
- Othello
- Connect Four
- chess 

## Requirements
 - TensorFlow (Tested on 1.15.0)  ( 2.0 or more recent cause a error in tensorflow so i recomend use a <2.0 )
 - NumPy
 - Python 3
 
## Usage
**To train the model from scratch.**:
```
python main.py --load_model 0
``` 

**To train the model using the previous best model as a starting point**:
```
python main.py --load_model 1
``` 

**To play a game vs the previous best model**:
```
python main.py --load_model 1 --human_play 1
``` 

