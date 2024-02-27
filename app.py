import streamlit as st
import random
import pandas as pd
from datetime import datetime
import time
import pytz



jeu = st.session_state.get('jeu',   'accueil'  ) 
#col1, col2 = st.columns(2)
#st.session_state.jeu = "easter egg"
   #///////////////////////////////
def actualiser():

    sante = st.session_state.get('sante', 50)
    nourriture = st.session_state.get('nourriture', 50)
    soif = st.session_state.get('soif', 50)
    physique = st.session_state.get('physique', 50)
    etat_mental = st.session_state.get('etat_mental', 50)
   
    etat = {  
        "santé💊" :      sante,
        "nourriture🌭":  nourriture,
        "soif🍹" :       soif,
        "physique🏃‍" :   physique,
        "état mental☺️": etat_mental 
    }
    #c = {
    #    "etat":"---------------------------------- VV Statistique VV --------------------------------------"
    #    }
    #if False:
    #    for i in etat:
    #        a = int ( int( (etat[str(i)]) )/1.15 )
    #        b = str(etat[str(i)])+"%"	#le debut de la bar des etats
    #        for j in range(int(a)):  #la longueur de la bar des etats
    #            b += "/"           
		

    #        c[str(i)] = b
    #    st.table(c)
    if True:
        st.markdown("""
        <style>
        stProgress .st-bo {
            background-color: green;
        }
        </style>
        """, unsafe_allow_html=True)
        for i in etat:
            a = int ( int( etat[str(i)] ))
            st.info(       f":green[{i}]: :red[{a}%]"          )
            progress = st.progress(a)
            #st.progress(a)
        
        


#____________savoir quel est le besoin qui est le plus petit_____________
 
    a = []
    for k , v in etat.items():
        a += [[k , v]]
    etat_besoin = "JHGFD"
    minimum = 70
    for i in a:
        if i[1] < minimum :
            minimum = i[1]
            etat_besoin = i[0]
    #st.write(minimum , etat_besoin)

#_________message afficher qui depend du besoin qui est le plus petit_______________
    valeur = minimum
    message = ""
    

    if etat_besoin == "santé💊":
        if valeur < 15:
            message = "il est  très malade"
        elif valeur < 25:
            message = "il est malade"
        elif valeur < 50:
            message ="il est un peu malade"
        else:
            message = "il est en bonne santé"
    elif etat_besoin == "nourriture🌭":
        if valeur < 15:
            message = "il a très faim"
        elif valeur < 25:
            message = "il a faim"
        elif valeur < 50:
            message ="il a un peu faim"
        else:
            message = "il est en bonne santé"
    elif etat_besoin == "soif🍹":
        if valeur < 15:
            message = "il a très soif"
        elif valeur < 25:
            message = "il a soif"
        elif valeur < 50:
            message ="il a un peu soif"
        else:
            message = "il est en bonne santé"
    elif etat_besoin == "physique🏃‍":
        if valeur < 15:
            message = "il n'est vraimment pas en forme"
        elif valeur < 25:
            message = "il n'est pas en forme"
        elif valeur < 50:
            message ="il est presque en forme"
        else:
            message = "il est en bonne santé"
    elif etat_besoin == "état mental☺️":
        if valeur < 15:
            message = "il n'est vraimment pas en bon état mental"
        elif valeur < 25:
            message = "il n'est pas en bon état mental"
        elif valeur < 50:
            message ="il est presque en bon état mental"
        else:
            message = "il est en bonne santé"
    else:
        message = "il est en bonne santé"

    st.warning(f">__>{message}<__")
    difficulte = st.session_state.get('difficulte','normal')

#_________l'image afficher qui depend du besoin qui est le plus petit_______________
    #//////// image -> normal

    VVVV = 400
    if difficulte == 'normal':
        if valeur < 40:
            st.image('sonicMal.png','',VVVV)
        else:
            st.image('sonicBien.png','',VVVV)
    #///////////image -> difficile
    if difficulte == 'difficil':
        if valeur < 40:
            st.image('shadowMal.png','',VVVV)
        else:
            st.image('shadowBien.png','',VVVV)
        
jeu = st.session_state.get('jeu',   'accueil'  )
   #////////////////////////////////   
def main():
    global etat , sante , nourriture , soif , physique , etat_mental ,jeu
    sante = st.session_state.get('sante', 50)
    nourriture = st.session_state.get('nourriture', 50)
    soif = st.session_state.get('soif', 50)
    physique = st.session_state.get('physique', 50)
    etat_mental = st.session_state.get('etat_mental', 50)
    
    if sante <= 0 or nourriture <= 0 or soif <= 0 or physique <= 0 or etat_mental <= 0:
        st.session_state.jeu = "mort"
        

    if jeu == 'accueil':
        st.title('Projet Tamagochi(NSI)')
        st.title(':green[page d accueil] ')
        st.write(':blue[EXPLICATION]')
        if st.button('clicker pour voir les explications'):
            st.session_state.jeu = "explication"
            st.rerun()
        difficulte = st.selectbox(":red[difficulté choisi]",("normal","difficil"))
        st.write(':blue[JOUER]')
                  
        if st.button('clicker pour commencer à jouer'):
            st.session_state.jeu = "nom"
            st.session_state.difficulte = difficulte
            st.rerun()
        st.write(':green[votre Tamagochi : ]')
        if difficulte == "normal":
            st.image('sonicChoix.png')
        elif difficulte == 'difficil':
            st.image('difficilChoix.png')
        
    elif jeu == 'explication':
        st.title(':green[page d explication] ')
        if st.button('clicker pour retourner à la page d accueil'):
            if random.randint(0 , 10) == 1:
                st.session_state.jeu = "easter egg"
                st.rerun()
            else:
                st.session_state.jeu = "accueil"
                st.rerun()
        st.title(':orange[But du jeu:]')
        st.write('>>:orange[Vous devez s occuper du Tamagochie pour qu il reste en vie ,en s occupant de ses besoins(sante,soif,nourriture,physique et etat mental)avant qu il atteint à 0% , en appuyant sur les boutons correspondant sur la page]')
        st.write('>>:orange[Les besoins du Tamagochie diminue au cours du temp(en fonction de la difficulté),si vous laissez le Tamagochie a avoir l une de ses besoins à atteindre 0% vous aurez perdu le jeu]')
        st.write('>>:orange[Pour le besoin **_-etat mental-_** vous allez jouer un jeu choisi entre 3 choix de jeu different(morpion , pierre feuille sciseau et trouver l intru]')
    elif jeu == "main":   
    
        #Nom_utilisateur = st.session_state.Nom_utilisateur('Nom_utilisateur','error4')
        difficulte = st.session_state.get('difficulte','normal')
            
        if difficulte == 'normal' :
            st.title('jeu en Mode: :red[normal]')
        elif difficulte == 'difficil':
            st.title('jeu en Mode: :red[difficil]')
                
        Nom_utilisateur = st.session_state.get('Nom_utilisateur',"ERROR4")
        if Nom_utilisateur == "2024":
            st.write(':red[>**__vous etes -2024- donc un developeur: vous avez acces a des chose privé__**]')
        st.header(f':green[bienvenu] :blue[**__{str( Nom_utilisateur )}__**] ')
        
        Nom_utilisateur = st.session_state.get('Nom_utilisateur',"ERROR4")
        col1 , col2 ,col3 ,col4 ,col5 = st.columns(5)
        col11 ,col22 ,col33 = st.columns(3)
        with col1:
            if st.button(':red[soigner]'):
                sante += 45
                st.toast('votre Tamagochie s est soigner') 
        with col2:
            if st.button(':red[manger]'):
                nourriture += 45
                st.toast('votre Tamagochie a mangé')         
        with col3:
            if st.button(':red[boire]'):
                soif += 45
                st.toast('votre Tamagochie s est soigner')
        with col4:
            if st.button(':red[sortir]'):
                physique += 25
                st.toast('votre Tamagochie s est sorti') 
        with col5:        
            if st.button(':red[jouer]'):
                jeu = "game"
                st.session_state.jeu = jeu
                st.rerun()
                #st.toast('votre Tamagochie a joué avec vous')      
        if Nom_utilisateur == "2024":
            with col11:
                if st.button(':orange[**__-TEST- reset__**]'):
                    sante = 100
                    nourriture = 100
                    soif = 100
                    physique = 100
                    etat_mental = 100
            with col22:
                if st.button('**__:orange[faire mourrir le tamagochie]__**'):
                    st.toast('clac mort')
                    st.session_state.jeu ="mort"
                    st.rerun()    
            with col33:
                if st.button('**__:orange[faire diminuer les stats]__**'):
                    st.session_state.sante += -10
                    st.session_state.nourriture += -10
                    st.session_state.soif += -10
                    st.session_state.physique += -10
                    st.session_state.etat_mental += -10
                    st.rerun()        
        #/////////////   
        if sante > 100:
            sante = 100
        if nourriture > 100:
            nourriture = 100
        if soif > 100:
            soif = 100
        if physique > 100:
            physique = 100
        if etat_mental > 100:
            etat_mental = 100   
        if sante <= 0 or nourriture <= 0 or soif <= 0 or physique <= 0 or etat_mental <= 0:
            st.session_state.jeu = "mort"
            st.rerun()
        #/////////////      
        etat = {  
            "santé💊" :      sante,
            "nourriture🌭":  nourriture,
            "soif🍹" :       soif,
            "physique🏃‍" :   physique,
            "état mental☺️": etat_mental 
        }     
        # Save variables to session state
        st.session_state.jeu = jeu
        st.session_state.sante = sante
        st.session_state.nourriture = nourriture
        st.session_state.soif = soif
        st.session_state.physique = physique
        st.session_state.etat_mental = etat_mental
    elif jeu == "game":
        #game = st.session_state.get('game', {"morpion":0,"pierre feuille ciseau":0,"trouver l intru(en 10sec)":0})
        game = {
            "morpion":0,
            "pierre feuille ciseau":0,
            "trouver l intru(en 10sec)":0
            }          
        playable_game = ["morpion","pierre feuille ciseau","trouver l intru(en 10sec)"]
        st.write('Vous voulez jouez avec votre tamagochie?🎮🎮🎰🎰')
        option = st.selectbox("choisi un jeu pour jouer",playable_game)
        if st.button("selectioné"):
            st.toast(f"vous avez choisi le {option} ")
            jeu = str(option)
            st.session_state.jeu = jeu
            st.rerun()
        st.write(f" :green[Tous les jeu joué]->  - :orange[ morpion]:{game['morpion']} - :orange[pierre feuille ciseau]:{game['pierre feuille ciseau']} - :orange[trouver l intru(en 10sec)]:{game['trouver l intru(en 10sec)']}"             )
        st.warning('Le jeu qui a été __joué le plus__ donnera __moin__ -etat mental-  :red[__(8 - 15 - 25 )__ ]                ')
        st.write('retour?')
        if st.button(':blue[Retour]'):
            st.session_state.jeu = "main"
            st.rerun()
        Nom_utilisateur = st.session_state.get('Nom_utilisateur','error4')
        if Nom_utilisateur == "2024":
            if st.button(':red[skip(pour les developeur  uniquement)]'):
                st.session_state.etat_mental += 25
                st.session_state.jeu = "main"
                st.rerun()

                
    #///////////////////////////////////////////////////
    elif jeu == "morpion":
        Nom_utilisateur = st.session_state.get('Nom_utilisateur',"ERROR4")
        st.write("morpion:red[(bugged -> probleme de saisie)]")
        st.write(":orange[But : avoir 3 sumbole sur une meme ligne ou meme cologne ou meme diagonale pour gagner]")
        winner = st.session_state.get('winner',"none")
        cadre = st.session_state.get('cadre',["(0)" ,"(1)" ,"(2)" ,"(3)" ,"(4)" ,"(5)" ,"(6)" ,"(7)" ,"(8)"])
        cadre_libre = st.session_state.get('cadre_libre',[ i for i in  range(9)])
        
        st.session_state.cadre = cadre
        st.session_state.cadre_libre = cadre_libre
        def win(x1 ,x2 ,x3 ):
            global winner ,cadre , cadre_libre
            cadre = (st.session_state.cadre)
            
            if cadre[x1] == "X" and cadre[x2] == "X" and cadre[x3] == "X":
                st.session_state.winner = "gagner"
                st.session_state.cadre = cadre
                st.session_state.cadre_libre = []
                st.rerun()
            elif cadre[x1] == "O" and cadre[x2] == "O" and cadre[x3] == "O":
                st.session_state.winner = "perdu"
                st.session_state.cadre = cadre
                st.session_state.cadre_libre = []
                st.rerun()
            else:
                st.session_state.winner = "none"

          
        def save_morp():
            st.session_state.cadre = cadre
            st.session_state.cadre_libre = cadre_libre
            st.rerun() 
        def ai_morp():
            global choix_ord ,cadre_libre ,cadre
            if not (st.session_state.cadre_libre) == []:
                lenght = len(st.session_state.cadre_libre)
                AA = random.randint(0,  int(lenght)-1 )
                choix_ord = (st.session_state.cadre_libre)[AA]
                (st.session_state.cadre)[choix_ord] = "O"
                (st.session_state.cadre_libre).remove(choix_ord) 
        
        if len(cadre_libre) == 9 and random.randint(0,1) == 0:
            ai_morp()
        
        for i in range(3):
            st.write(f".{cadre[i*3]}.    /    .{cadre[i*3 +1]}.   /   .{cadre[i*3 +2]}.")
            
       
        if not(len(cadre_libre) == 0):
            
            #choix = st.selectbox("choix:",cadre_libre)#Partie utilisateur VV
            choix = int(st.text_input('n°case'))
            if st.button('choisir')and( choix in cadre_libre):
                cadre[choix] = "X"
                cadre_libre.remove(choix)       

                #cadre_libre = CADRE_1 
                        
                win(0 , 1 , 2 )
                win(3 , 4 , 5 )
                win(6 , 7 , 8 )
                    
                win(0 , 3 , 6 )
                win(1 , 4 , 7 )
                win(2 , 5 , 8 )
                    
                win(0 , 4 , 8 )
                win(2 , 4 , 6 )
     
                ai_morp()#----------Partie Tamagochi
                                                                      
                win(0 , 1 , 2 )
                win(3 , 4 , 5 )
                win(6 , 7 , 8 )
                    
                win(0 , 3 , 6 )
                win(1 , 4 , 7 )
                win(2 , 5 , 8 )
                    
                win(0 , 4 , 8 )
                win(2 , 4 , 6 )
                save_morp()                          

        else:   
            st.write('La parti est fini')
            if winner == "égalité":
                st.info('égalité')
            if winner == "perdu":
                st.error(f'{Nom_utilisateur} a perdu')
            if winner == "gagner":
                st.success(f'{Nom_utilisateur} a gagner')
            st.balloons()
            if True:    
                time.sleep(5)
                jeu = "main"
                st.session_state.jeu = jeu
                st.session_state.cadre = ["(0)" ,"(1)" ,"(2)" ,"(3)" ,"(4)" ,"(5)" ,"(6)" ,"(7)" ,"(8)"]
                st.session_state.cadre_libre = [ i for i in  range(9)]
                #st.session_state.etat_mental = etat_mental + 25
                game = st.session_state.get('game', {"morpion":0,"pierre feuille ciseau":0,"trouver l intru(en 5sec)":0})
                if game['morpion'] > game['pierre feuille ciseau'] and game['morpion'] > game['trouver l intru(en 5sec)']:
                    st.session_state.etat_mental = etat_mental + 9
                elif game['morpion'] < game['pierre feuille ciseau'] and game['morpion'] < game['trouver l intru(en 5sec)']:
                    st.session_state.etat_mental = etat_mental + 25
                else:
                    st.session_state.etat_mental = etat_mental + 15
                game['morpion'] += 1
                st.session_state.game = game
                st.rerun()  
            else:
                if st.button('TEST-restart'):
                    jeu = "morpion"
                    st.session_state.jeu = jeu
                    st.session_state.cadre = ["(0)" ,"(1)" ,"(2)" ,"(3)" ,"(4)" ,"(5)" ,"(6)" ,"(7)" ,"(8)"]
                    st.session_state.cadre_libre = [ i for i in  range(9)]
                    st.rerun()
 
    elif jeu == "pierre feuille ciseau":
        Nom_utilisateur = st.session_state.get('Nom_utilisateur',"ERROR4")
        def fin():
            time.sleep(5)
            st.session_state.score = [0 , 0 ]
            jeu = "main"
            st.session_state.jeu = jeu
            #st.session_state.etat_mental = etat_mental + 25
            game = st.session_state.get('game', {"morpion":0,"pierre feuille ciseau":0,"trouver l intru(en 5sec)":0})
            if game['pierre feuille ciseau'] > game['morpion'] and game['pierre feuille ciseau'] > game['trouver l intru(en 5sec)']:
                st.session_state.etat_mental = etat_mental + 9
            elif game['pierre feuille ciseau'] < game['morpion'] and game['pierre feuille ciseau'] < game['trouver l intru(en 5sec)']:
                st.session_state.etat_mental = etat_mental + 25
            else:
                st.session_state.etat_mental = etat_mental + 15
            game['pierre feuille ciseau'] += 1
            st.session_state.game = game
            st.rerun()
        def parti_suivt(X):
            time.sleep(5)
            jeu = "pierre feuille ciseau"
            if X == 0:
                st.session_state.score = [ score[0] + 1 , score[1] ]
            elif X == 1 :
                st.session_state.score = [ score[0]  , score[1] + 1 ]
            st.session_state.jeu = jeu
            st.session_state.parti_NB = parti_NB + 1
            st.rerun()
                
        score = st.session_state.get('score', [ 0 , 0 ])
        parti_NB = st.session_state.get('parti_NB', 0 )
        
        if not(parti_NB == 3):
            st.write("pierre feuille ciseau")
            st.write(":orange[But : choisir une des objets pour gagner ,en fonction des objets que vous et le tamagochie a choisi essayer de gagner] ")
            st.write(":blue[feuille > pierre > ciseau]")
            st.write(":blue[ciseau > feuille > pierre]")
            st.write(":blue[pierre > ciseau > feuille] ")
            
            a = random.randint(1, 3)
            if a == 1:
                choix_ord = "pierre"
            elif a == 2:
                choix_ord = "feuille"
            elif a == 3:
                choix_ord = "ciseau"
                

            choix = st.selectbox("choix:",["pierre","feuille","ciseau"])
            st.write(f"Partie numero: {parti_NB}")
            st.write(f":green[score] :   {Nom_utilisateur}:{score[1]} - Tamagochie{score[0]}")
            if st.button('choix choisi'):
                st.write(f"le tamagochi a choisi >{choix_ord}<")   
                st.write(f"{Nom_utilisateur} as choisi >{choix}<: ")   
                if choix == choix_ord:
                    st.warning('egalié')
                    st.session_state.score = [ score[0]  , score[1]]
                    st.session_state.jeu = jeu
                    st.rerun()
                

                if choix == "ciseau":
                    if choix_ord == "feuille":
                        st.success(f'{Nom_utilisateur} a Gagner')
                        st.balloons()
                        parti_suivt(1)
                    if choix_ord == "pierre":
                        st.error(f'{Nom_utilisateur} a Perdu')
                        parti_suivt(0)
                        
                if choix == "pierre":
                    if choix_ord == "feuille":
                        st.error(f'{Nom_utilisateur} a Perdu')
                        parti_suivt(0)
                    if choix_ord == "ciseau":
                        st.success(f'{Nom_utilisateur} a Gagner')
                        st.balloons()
                        parti_suivt(1)
                        
                if choix == "feuille":
                    if choix_ord == "ciseau":
                        st.error(f'{Nom_utilisateur} a Perdu')
                        parti_suivt(0)
                    if choix_ord == "pierre":
                        st.success(f'{Nom_utilisateur} a Gagner')
                        st.balloons()
                        parti_suivt(1)
        else:
            if score[1] == score[0] :
                st.warning('le Match est un égalité')
            if score[1] > score[0] :
                st.success(f'{Nom_utilisateur} a gagnez le Match')
            if score[1] < score[0] :
                st.error(f'{Nom_utilisateur} a perdu le Match')
            st.session_state.score = [0 , 0]
            st.session_state.parti_NB = 0
            fin()
    elif jeu == "trouver l intru(en 10sec)":
        st.write('essayez de trouver l intru')
        st.warning('essayer de trouver l intru dans la liste qui va s afficher , quand vous l aviez trouver ecrit le nomde la case dans le textinput et appuyez sur le boutton saisir')
        st.warning('Bonne chance vous avez 10 SECONDE !! ')
        time.sleep(10)
        st.session_state.jeu = "AZERTY"
        st.rerun()
    elif jeu == "AZERTY":
        st.write('essayez de trouver l intru')
        mode = st.session_state.get('mode', "start")
        if mode == "start":
            plat = st.session_state.get('plat', [])
            for i in range(40):
                plat+=["O"]
            intru = random.randint(0,len(plat)-1)
            plat[intru] = "Q"
            mode = "play"
            st.session_state.plat = plat
            st.session_state.mode = mode
            st.rerun()
        elif mode == "play":
            TIME_UP = 0
            plat = st.session_state.get('plat', [])
            st.write('----A_.B_C_D_E_.F_G_H_.I_.J------          ')
            
            for j in range(4):
                BB = ""
                for i in range(10):
                    BB += str(plat[j*10 + i]) +"_"
                st.write(f"{j}//{BB}")
            #st.write(plat)   
            cadre_S = ""
            cadre_S = st.text_input('case?(NombreLetrre ,exemple A7)')
            def convert_case(cadre_S):
                cc = int(cadre_S[1]) * 10
                if cadre_S[0] == "A":
                    cc += 0
                elif cadre_S[0] == "B":
                    cc += 1
                elif cadre_S[0] == "C":
                    cc += 2
                elif cadre_S[0] == "D":
                    cc += 3
                elif cadre_S[0] == "E":
                    cc += 4
                elif cadre_S[0] == "F":
                    cc += 5
                elif cadre_S[0] == "G":
                    cc += 6
                elif cadre_S[0] == "H":
                    cc += 7
                elif cadre_S[0] == "I":
                    cc += 8
                elif cadre_S[0] == "J":
                    cc += 9 
                return cc
            
            def finished():
                plat = []
                mode = "start"
                jeu = "main"
                st.session_state.plat = plat
                st.session_state.mode = mode
                st.session_state.jeu = jeu
                #st.session_state.etat_mental = etat_mental + 25
                game = st.session_state.get('game', {"morpion":0,"pierre feuille ciseau":0,"trouver l intru(en 10sec)":0})
                if game['trouver l intru(en 10sec)'] > game['morpion'] and game['trouver l intru(en 10sec)'] < game['pierre feuille ciseau']:
                    st.session_state.etat_mental = etat_mental + 9
                elif game['trouver l intru(en 10sec)'] < game['morpion'] and game['trouver l intru(en 10sec)'] < game['pierre feuille ciseau']:
                    st.session_state.etat_mental = etat_mental + 25
                else:
                    st.session_state.etat_mental = etat_mental + 15
                game['trouver l intru(en 10sec)'] += 1
                st.session_state.game = game
                st.rerun()
            if st.button('saisir') and not( TIME_UP == 1)                 :
                if (plat[convert_case(cadre_S)] == "Q" ):
                    st.success('VOUS AVEZ REUSSI A TROUVER L INTRU , BRAVO!!!')
                    st.balloons()
                    time.sleep(5)
                    finished()
                else:
                    st.toast('VOUS N AVIEZ PAS A TROUVER L INTRU , DOMMAGE!!!')
                    finished()
            bar = st.progress(0)        
            for i in range(100):
                bar.progress(i)  
                time.sleep(0.1)
                bar.empty()
            TIME_UP = 1
            st.toast('VOUS N AVIEZ PAS A TROUVER L INTRU A TEMPS, DOMMAGE!!!')
            finished()
    elif jeu == "easter egg" :
        st.title(':green[EASTER EGG PAGE]')
        st.write(':orange[VOUS AVEZ REUSSI A TROUVER LA PAGE DE L EASTER EGG]')
        if st.button('**__:red[retour page accueil]__**'):
            jeu = "accueil"
            st.session_state.jeu = jeu
            st.rerun()
        HHH = "azertyuiopmlkjhgfdsqnbvcxwAZERTYUIOPMLKJHGFDSQWXCVBN1234567890°+=)àç_è-(\¨µ£%ù*$"
        JJJ = ""
        for i in range(10000):
            JJJ += HHH[random.randint(0 , len(HHH)-1)]
        st.write(f":red[{JJJ}]") 
        while True:
            
            time.sleep(0.5)
            GGG = ""
           
            for i in range(100):
                GGG += HHH[random.randint(0 , len(HHH)-1)]
            LLL = random.randint(0,6)
            if LLL ==0:
                st.toast(f":red[{GGG}]") 
            elif LLL ==1:
                st.toast(f":orange[{GGG}]") 
            elif LLL ==2:
                st.toast(f":yellow[{GGG}]") 
            elif LLL ==3:
                st.toast(f":green[{GGG}]") 
            elif LLL ==4:
                st.toast(f":cyan[{GGG}]") 
            elif LLL ==5:
                st.toast(f":blue[{GGG}]")
            else:
                st.toast(GGG)
            if random.randint(0,3)==1:
                st.toast("**___:orange[!!!!!!!!!!!!!!!!!!!!Les developpeurs de ce jeu sont les meilleurs!!!!!!!!!!!!!!!!]__**")
    elif jeu == "nom":
    
        Nom_utilisateur  = st.text_input(':orange[saisir votre nom d utilisateur]')
        if st.button('**__:green[Saisir et commencez]__**') :          
            if not(Nom_utilisateur == ''):
                st.session_state.Nom_utilisateur = str(Nom_utilisateur  )
                st.toast(f'bienvenu {Nom_utilisateur}')
                st.session_state.jeu = "main"
                st.rerun()
            elif Nom_utilisateur == '':
                st.error('Veuillez saisir un __nom__')
    elif jeu == "mort":
        if st.button('**__:green[Voulez vous aller à la page d accueil?]__**'):
            st.session_state.jeu = "accueil"
            st.session_state.sante = 50
            st.session_state.nourriture = 50
            st.session_state.soif = 50
            st.session_state.physique = 50
            st.session_state.etat_mental = 50
            st.session_state.difficulte = "normal"
            st.rerun()
        st.toast('VOTRE TAMAGOCHIE EST MORT')
        difficulte = st.session_state.get('difficulte',"none")
        col111 ,col222 ,col333 = st.columns(3)
        with col222:
            if difficulte == 'normal':
                st.image('SonicMort','',400)
            elif difficulte == 'difficil':
                st.image('ShadowMort','',400)
        #for i in range(20):
        st.error('>>>>>>>>>>:orange[_>>VOTRE TAMAGOCHIE EST __**MORT**__<<_]') 
        while True:#Pour eviter que les bouton ne fonctionnent pas
            time.sleep(2)
    
    
     #/////////////////////////////////////////////////////      
if True :
    main()
    if jeu == "main":
        actualiser()  
    while not (jeu == "main") : #Pour eviter que les bouton ne fonctionnent pas
        time.sleep(5)
if jeu == "main":
    #time.sleep(10)
    #bar = st.progress(0)   
    if st.button(':green[**__Voulez vous quitter partie ?__**] :red[Si vous appuyez sur le bouttons tout votre progres vont être perdu , en êtes-vous sûre?]'):
        st.toast(':green[Vous avez quittez la parti!]')
        st.session_state.jeu = "accueil"
        st.session_state.sante = 50
        st.session_state.nourriture = 50
        st.session_state.soif = 50
        st.session_state.physique = 50
        st.session_state.etat_mental = 50
        st.session_state.difficulte = "normal"
        st.rerun()
    difficulte = st.session_state.get('difficulte','normal')
    bar = st.progress(0)
    if difficulte == 'normal':
        st.info('tous les :red[10sec] les statistiques :red[diminue]')
        for i in range(100):
            
            bar.progress(i)  
            time.sleep(0.1)
            bar.empty()
            #bar.progress(i)
    elif difficulte == 'difficil':
        st.info('tous les :red[5sec] les statistiques :red[diminue (de 4% à 10%)]')
        for i in range(100):
            
            bar.progress(i)  
            time.sleep(0.05)
            bar.empty()
            #bar.progress(i)   
    global etat , sante , nourriture , soif , physique , etat_mental
    sante +=        - random.randint(4, 10)
    nourriture +=   - random.randint(4 , 10)
    soif +=         - random.randint(4 , 10)
    physique +=     - random.randint(4 , 10)
    etat_mental +=  - random.randint(4 , 10)

    st.session_state.sante = sante
    st.session_state.nourriture = nourriture
    st.session_state.soif = soif
    st.session_state.physique = physique
    st.session_state.etat_mental = etat_mental

    st.rerun()


        
    #TEXT

    #st.text("chose à faire :")
    #st.text("régler le probleme d'actualiser la page (comment sauvegarder les modification des etats apres un boutton qui a etet appuyyer")
    #st.text("importer les images du tamagochie  ")
    #st.text("un timer qui modifie les etats apres un certain temps  ")


	



