import streamlit as st
from math import sqrt, log, pi, exp
from interpolazione import conducibilita_termica_interpolata
import pandas as pd
import csv
import altair as alt
from datetime import datetime



# routine di calcolo irraggiamento
def Irraggiamento(T, Ta, Ts, e):

    if (T >= Ta):
        Qr = 5.67 * e * ((((Ts + 273.15) / 100) ** 4) - (((Ta + 273.15) / 100) ** 4))   
    else:
        Qr = 5.67 * e * ((((Ta + 273.15) / 100) ** 4) - (((Ts + 273.15) / 100) ** 4))

       
    return Qr

# routine di calcolo convezione
def Convezione(T, Ta, Ts, W):

    if (T >= Ta):
        Qcv = 1.94 * ((Ts + 273.15) - (Ta + 273.15)) ** 1.25 * sqrt((W + 1.26) / 1.26)
    else:
        Qcv = 1.94 * ((Ta + 273.15) - (Ts + 273.15)) ** 1.25 * sqrt((W + 1.26) / 1.26)

    return Qcv


# routine di calcolo conduzione
def Conduzione(numlayers, T, Ta, Ts, Cond_Tubo, D_Metallo, D_Fluido, K1, K2, K3, K4, K5, d1, d2, d3, d4, d5, Cond_Finitura, D_Finitura):

    if (numlayers ==0):
        if (T > Ta):
            Qcd = (((T + 273.15) - (Ts + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d1))))
        else:
            Qcd = (((Ts + 273.15) - (T + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d1))))
  

    if (numlayers ==1):
        if (T > Ta):
            Qcd = (((T + 273.15) - (Ts + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d1))))
        else:
            Qcd = (((Ts + 273.15) - (T + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d1))))
 

    if (numlayers ==2):
        if (T > Ta):
            Qcd = (((T + 273.15) - (Ts + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * K2)) * (log(d2 / d1))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d2))))
        else:
            Qcd = (((Ts + 273.15) - (T + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * K2)) * (log(d2 / d1))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d2))))        

    if (numlayers ==3):
        if (T > Ta):
            Qcd = (((T + 273.15) - (Ts + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * K2)) * (log(d2 / d1))) + ((1 / (2 * K3)) * (log(d3 / d2))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d3))))
        else:
            Qcd = (((Ts + 273.15) - (T + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * K2)) * (log(d2 / d1))) + ((1 / (2 * K3)) * (log(d3 / d2))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d3))))        

    if (numlayers ==4):
        if (T > Ta):
            Qcd = (((T + 273.15) - (Ts + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * K2)) * (log(d2 / d1))) + ((1 / (2 * K3)) * (log(d3 / d2))) + ((1 / (2 * K4)) * (log(d4 / d3))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d4))))
        else:
           Qcd = (((Ts + 273.15) - (T + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * K2)) * (log(d2 / d1))) + ((1 / (2 * K3)) * (log(d3 / d2))) + ((1 / (2 * K4)) * (log(d4 / d3))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d4))))

    if (numlayers ==5):
        if (T > Ta):
            Qcd = (((T + 273.15) - (Ts + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * K2)) * (log(d2 / d1))) + ((1 / (2 * K3)) * (log(d3 / d2))) + ((1 / (2 * K4)) * (log(d4 / d3))) + ((1 / (2 * K5)) * (log(d5 / d4))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d5))))
        else:
            Qcd = (((Ts + 273.15) - (T + 273.15)) * pi) / (((1 / (2 * Cond_Tubo)) * (log(D_Metallo / D_Fluido))) + ((1 / (2 * K1)) * (log(d1 / D_Metallo))) + ((1 / (2 * K2)) * (log(d2 / d1))) + ((1 / (2 * K3)) * (log(d3 / d2))) + ((1 / (2 * K4)) * (log(d4 / d3))) + ((1 / (2 * K5)) * (log(d5 / d4))) + ((1 / (2 * Cond_Finitura)) * (log(D_Finitura / d5))))

    return Qcd

# routine di calcolo dispersione termica
def Dispersione(section, W, numTratti, LTratto, numlayers, Tr, Ta, Cond_Tubo, OD, ID, thk, codei1, codei2, codei3, codei4, codei5, thki1, thki2, thki3, thki4, thki5, d1, d2, d3, d4, d5, condFinish, thkFinish, DFinish, emissivity, P, cal_spc, autoTF):
    
    if 'output' not in st.session_state:
        st.session_state.output = []    
    if 'dfOut' not in st.session_state:
        st.session_state.dfOut = ""
    if 'lprog' not in st.session_state:
        st.session_state.lprog = 0.00   
    if 'TF' not in st.session_state:
        st.session_state.TF = 0.00
    if 'T1' not in st.session_state:
        st.session_state.T1 = 0.00

   
    delta_Ts = 0.1
    e = emissivity
    if section == 0:
        T = Tr
        st.session_state.T1 = Tr
    else:
        print('sect., Tr, TF, media ', section, Tr, st.session_state.TF, (Tr + st.session_state.TF)/2)
        if autoTF == False:
            T = (Tr + st.session_state.TF)/2
            st.warning(f'For section {section} the temperature considered at the start is {T}')
        elif autoTF == True:
            T = st.session_state.TF 


    file_csv = 'files/Cond_Isolanti.csv' 

    #**********************************************
    #* Caso di assenza di isolamento termico ******

    if (numlayers ==0):      # assenza isolamento termico
    

        Punto_Iniziale = 0
        Punto_Finale = 0
        Qcd_Tratto = 0.00
        progress_text = st.empty()
        
        for tratto in range(numTratti):

            percent_complete = (tratto+1)/(numTratti)*100
            progress_text.text(f"Progress: segment {tratto+1} of {numTratti} - ({percent_complete}%)")
            #st.write('tratto, numTratti' , tratto, numTratti)
            st.session_state.lprog = st.session_state.lprog + LTratto
           
            #st.write('tratto, T ', tratto, T)
            Ts = Ta
            #Tp_Metallo = (T - Ta) * (thk + thki1 + thkFinish) / (thk + thki1 + thkFinish)
            Tp_Metallo = (T - Ta) * (thk + thkFinish) / (thk + thkFinish)    # thki1 = 0
            # Tp1 = (T - Ta) * (thki1 + thkFinish) / (thk + thki1 + thkFinish)  # non esiste isolamento termico
            #Tp_Finitura = (T - Ta) * (thkFinish) / (thk + thki1 + thkFinish)
            Tp_Finitura = (T - Ta) * (thkFinish) / (thk + thkFinish)

            Port = P
            verifica = 1.5

            while not verifica <= 0:
                if T >= Ta:
                    Ts = Ts + delta_Ts
                elif T < Ta:
                    Ts = Ts-delta_Ts

                Qr =  Irraggiamento(T, Ta, Ts, e)
                Qcv = Convezione(T, Ta, Ts, W)
                Ae = (Qr + Qcv)
                #temp_media = (T + Tp1) / 2
                temp_media = (T + Tp_Finitura) / 2
                #codice_mat = codei1
                #condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K1 = 0.1
                K2 = 0
                K3 = 0
                K4 = 0
                K5 = 0

                Qcd = Conduzione(numlayers, T, Ta, Ts, Cond_Tubo, OD, ID, K1, K2, K3, K4, K5, d1, d2, d3, d4, d5, condFinish, DFinish)   


                if T > Ta:

                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    # Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))   # non esiste isolamento
                    Dt1 = 0.0
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T - (Dt_Metallo)
                    Tp1 = T - (Dt_Metallo + Dt1)
                    Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt_Finitura)
        
                else:        
                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    # Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt1 = 0.0
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
    
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T + (Dt_Metallo)
                    Tp1 = T + (Dt_Metallo + Dt1)
                    Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt_Finitura)

            # Dal codice sopra esce qaundo 'verifica <= 0' ed esegue il codice sottostante
            # -----------------------------
            Qcd1 = Qcd
            Cal_Disp_Kcal = Qcd1 * 0.5898452
            Punto_Iniziale = Punto_Finale
            Punto_Finale = Punto_Iniziale + LTratto

                        # valori inizio tratto
            Tiniziale = T
            Tf_precedente = st.session_state.TF
            TpMi = Tp_Metallo
            Tp1i = Tp1
            TpFi = Tp_Finitura


            if (section == 0 and tratto == 0):
                #st.session_state.lprog = 0
                st.session_state['output'] = [{
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': 0,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ts': TpFi
                }]

                        # caso in cui per la sezione si inserisce una temperatura diversa dal tratto precednte
            if (section > 0 and tratto == 0 and Tiniziale != Tf_precedente):
                #st.session_state.lprog = 0
                st.session_state['output'].append ({
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': st.session_state.lprog - LTratto,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ts': TpFi
                })    

            if T >= Ta :
                X2 = exp((-LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = T
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)
                
                Tp_Metallo = T - (Dt_Metallo)
                # Tp1 = T - (Dt_Metallo + Dt1) : non esiste isolamento
                Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt_Finitura)
    
            else:    
                X2 = exp((LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = T
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                Tp_Metallo = T + (Dt_Metallo)
                # Tp1 = T + (Dt_Metallo + Dt1)  non esiste isolamento
                Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt_Finitura)

            Lprogressiva = st.session_state.lprog
            Tpiso1 = "nd"
            Tpiso2 = "nd"
            Tpiso3 = "nd"
            Tpiso4 = "nd"
            Tpiso5 = "nd"
          
            st.session_state['output'].append({
            #    'ID': st.session_state.num_tratto-1,
                'Section': section,
                'Segment': tratto,
                'Length': LTratto,
                'L_Progr': Lprogressiva,
                'Qcd': Qcd,
                'Qcd_segment': Qcd_Tratto,
                'Tf': T,
                'Tmetal': Tp_Metallo,
                
                'Ts': Tp_Finitura
            })

        st.session_state.dfOut = pd.DataFrame(st.session_state['output'])
        #st.dataframe(st.session_state.dfOut, hide_index= False)    
        st.session_state.dfOut.to_csv('files/Output.csv')   # salva dati su Output.csv      
    
        return Qcd_Tratto, Tfinale                 
    
    
    # Caso di uno strato di isolante termico    
    if (numlayers ==1):
    
        Punto_Iniziale = 0
        Punto_Finale = 0
        Qcd_Tratto = 0.00
        # Inizializza la progress bar con valore 0
        #progress_bar = st.progress(0)
        progress_text = st.empty()


        for tratto in range(numTratti):
            # Calcola la percentuale di completamento
            #if numTratti!=0:
            #    percent_complete = int((tratto/ (numTratti)) * 100)
            #elif numTratti!=1:
            #    percent_complete = int((tratto/ (numTratti-1)) * 100)
            
            percent_complete = (tratto+1)/(numTratti)*100
            # Aggiorna la progress bar
            #progress_bar.progress(percent_complete)
            #progress_text.text(f"Progress: {tratto+1}/{numTratti} ({percent_complete}%)")
            progress_text.text(f"Progress: segment {tratto+1} of {numTratti} - ({percent_complete}%)")

            st.session_state.lprog = st.session_state.lprog + LTratto
           
            Ts = Ta
            Tp_Metallo = (T - Ta) * (thk + thki1 + thkFinish) / (thk + thki1 + thkFinish)
            Tp1 = (T - Ta) * (thki1 + thkFinish) / (thk + thki1 + thkFinish)
            Tp_Finitura = (T - Ta) * (thkFinish) / (thk + thki1 + thkFinish)
            Port = P
            verifica = 1.5
            Qr = 0
            Qcv = 0
            Qcd = 0

            while not verifica <= 0:
                if T >= Ta:
                    Ts = Ts + delta_Ts
                elif T < Ta:
                    Ts = Ts-delta_Ts

                Qr =  Irraggiamento(T, Ta, Ts, e)
                Qcv = Convezione(T, Ta, Ts, W)
                Ae = (Qr + Qcv)

                temp_media = (T + Tp1) / 2
                codice_mat = codei1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                
                K1 = condIso_media
                #K1 = 0.1189
                K2 = 0
                K3 = 0
                K4 = 0
                K5 = 0
                if isinstance(condIso_media, str):
                    st.error(f'The isolant code {codei1} is not compatible with temperature. Please change it before proceed.')
                    st.write('K1 = ', K1)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                #    print("La variabile è una stringa.")
                #    print(condIso_media)
                #else:
                #    print(f"La conducibilità termica per {codice_mat} a {temp_media}°C è {condIso_media:.4f}")
                Qcd = Conduzione(numlayers, T, Ta, Ts, Cond_Tubo, OD, ID, K1, K2, K3, K4, K5, d1, d2, d3, d4, d5, condFinish, DFinish)   

                if T > Ta:

                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T - (Dt_Metallo)
                    Tp1 = T - (Dt_Metallo + Dt1)
                    Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt_Finitura)
        
                else:        
                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
    
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T + (Dt_Metallo)
                    Tp1 = T + (Dt_Metallo + Dt1)
                    Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt_Finitura)


            # *****  Dal codice sopra esce quando 'verifica <= 0' ed esegue il codice sottostante ******
            # -----------------------------
            Qcd1 = Qcd
            Cal_Disp_Kcal = Qcd1 * 0.5898452
            Punto_Iniziale = Punto_Finale
            Punto_Finale = Punto_Iniziale + LTratto
            # valori inizio tratto
            Tiniziale = T
            Tf_precedente = st.session_state.TF
            TpMi = Tp_Metallo
            Tp1i = Tp1
            TpFi = Tp_Finitura



            if (section == 0 and tratto == 0):
                #st.session_state.lprog = 0
                st.session_state['output'] = [{
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': 0,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ts': TpFi
                }]
            # caso in cui per la sezione si inserisce una temperatura diversa dal tratto precednte
            if (section > 0 and tratto == 0 and Tiniziale != Tf_precedente):
                #st.session_state.lprog = 0
                st.session_state['output'].append ({
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': st.session_state.lprog - LTratto,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ts': TpFi
                })

            if T >= Ta :
                X2 = exp((-LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                # calcolo valori finali temperatura sulle varie interfacce
                #Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                #Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                #Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
       
                Tp_Metallo = T - (Dt_Metallo)
                Tp1 = T - (Dt_Metallo + Dt1)
                Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt_Finitura)

                
            else:    
                X2 = exp((LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                 # calcolo valori finali temperatura sulle varie interfacce
                Tp_Metallo = T + (Dt_Metallo)
                Tp1 = T + (Dt_Metallo + Dt1)
                Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt_Finitura)

            valoreEstratto = float(K1)

            Lprogressiva = st.session_state.lprog
            
            st.session_state['output'].append({
            #    'ID': st.session_state.num_tratto-1,
                'Section': section,
                'Segment': tratto,
                'Length': LTratto,
                'L_Progr': Lprogressiva,
                'Qcd': Qcd,
                'Qcd_segment': Qcd_Tratto,
                'Tf': T,
                'Tmetal': Tp_Metallo,
                'Ti1': Tp1,
                'Ts': Tp_Finitura
            })
                

        return Qcd_Tratto, Tfinale                     

    # Caso di due strati di isolante termico
    if (numlayers ==2):
        Punto_Iniziale = 0
        Punto_Finale = 0
        Qcd_Tratto = 0.00
        # Inizializza la progress bar con valore 0
        #progress_bar = st.progress(0)
        progress_text = st.empty()

        for tratto in range(numTratti):
            # Calcola la percentuale di completamento
            #if numTratti==0:
            #    percent_complete = int((tratto/ (numTratti)) * 100)
            #elif numTratti!=0:
            #    percent_complete = int((tratto/ (numTratti-1)) * 100)
            
            percent_complete = (tratto+1)/(numTratti) * 100
            # Aggiorna la progress bar
            #progress_bar.progress(percent_complete)
            #progress_text.text(f"Progress: {tratto+1}/{numTratti} ({percent_complete}%)")
            progress_text.text(f"Progress: segment {tratto+1} of {numTratti} - ({percent_complete}%)")

            st.session_state.lprog = st.session_state.lprog + LTratto
           
            Ts = Ta
            Tp_Metallo = (T - Ta) * (thk + thki1 + thki2 + thkFinish) / (thk + thki1 + thki2 + thkFinish)
            Tp1 = (T - Ta) * (thki1 + thki2 + thkFinish) / (thk + thki1 + thki2 + thkFinish)
            Tp2 = (T - Ta) * (thki2 + thkFinish) / (thk + thki1 + thki2 + thkFinish)
            Tp_Finitura = (T - Ta) * (thkFinish) / (thk + thki1 + thki2 + thkFinish)

            Port = P
            verifica = 1.5
            Qr = 0
            Qcv = 0
            Qcd = 0

            while not verifica <= 0:
                if T >= Ta:
                    Ts = Ts + delta_Ts
                elif T < Ta:
                    Ts = Ts-delta_Ts

                Qr =  Irraggiamento(T, Ta, Ts, e)
                Qcv = Convezione(T, Ta, Ts, W)
                Ae = (Qr + Qcv)

                temp_media = (T + Tp1) / 2
                # Trova K1
                codice_mat = codei1  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K1 = condIso_media
                if isinstance(condIso_media, str):
                    st.error(f'The isolant code {codei1} is not compatible with temperature. Please change it before proceed.')
                    st.write('K1 = ', K1)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K2
                codice_mat = codei2  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K2 = condIso_media
                K3 = 0
                K4 = 0
                K5 = 0
                if isinstance(condIso_media, str):
                    st.error(f'The isolant code {codei2} is not compatible with temperature. Please change it before proceed.')
                    st.write('K2 = ', K2)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                #    print("La variabile è una stringa.")
                #    print(condIso_media)
                #else:
                #    print(f"La conducibilità termica per {codice_mat} a {temp_media}°C è {condIso_media:.4f}")
                Qcd = Conduzione(numlayers, T, Ta, Ts, Cond_Tubo, OD, ID, K1, K2, K3, K4, K5, d1, d2, d3, d4, d5, condFinish, DFinish)   

                if T > Ta:

                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt2 = ((Qcd / pi) * ((1 / (2 * K2)) * (log((d2 / d1)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d2)))))
       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T - (Dt_Metallo)
                    Tp1 = T - (Dt_Metallo + Dt1)
                    Tp2 = T - (Dt_Metallo + Dt1 + Dt2)
                    Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt2 + Dt_Finitura)
        
                else:        
                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt2 = ((Qcd / pi) * ((1 / (2 * K2)) * (log((d2 / d1)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d2)))))
       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T + (Dt_Metallo)
                    Tp1 = T + (Dt_Metallo + Dt1)
                    Tp2 = T + (Dt_Metallo + Dt1 + Dt2)
                    Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt2 + Dt_Finitura)


            # *****  Dal codice sopra esce qaundo 'verifica <= 0' ed esegue il codice sottostante ******
            # -----------------------------
            Qcd1 = Qcd
            Cal_Disp_Kcal = Qcd1 * 0.5898452
            Punto_Iniziale = Punto_Finale
            Punto_Finale = Punto_Iniziale + LTratto
            # valori inizio tratto
            Tiniziale = T
            Tf_precedente = st.session_state.TF
            TpMi = Tp_Metallo
            Tp1i = Tp1
            Tp2i = Tp2
            TpFi = Tp_Finitura

            if (section == 0 and tratto == 0):
                #st.session_state.lprog = 0
                st.session_state['output'] = [{
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': 0,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ti2': Tp2i,
                    'Ts': TpFi
                }]
            # caso in cui per la sezione si inserisce una temperatura diversa dal tratto precednte
            if (section > 0 and tratto == 0 and Tiniziale != Tf_precedente):
                #st.session_state.lprog = 0
                st.session_state['output'].append ({
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': st.session_state.lprog - LTratto,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ti2': Tp2i,
                    'Ts': TpFi
                })

            if T >= Ta :
                X2 = exp((-LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                # calcolo valori finali temperatura sulle varie interfacce
                #Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                #Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                #Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
       
                Tp_Metallo = T - (Dt_Metallo)
                Tp1 = T - (Dt_Metallo + Dt1)
                Tp2 = T - (Dt_Metallo + Dt1 + Dt2)
                Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt2 + Dt_Finitura)

                
            else:    
                X2 = exp((LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                 # calcolo valori finali temperatura sulle varie interfacce
                Tp_Metallo = T + (Dt_Metallo)
                Tp1 = T + (Dt_Metallo + Dt1)
                Tp2 = T + (Dt_Metallo + Dt1 + Dt2)
                Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt2 + Dt_Finitura)

            valoreEstratto = float(K1)

            Lprogressiva = st.session_state.lprog
            
            st.session_state['output'].append({
            #    'ID': st.session_state.num_tratto-1,
                'Section': section,
                'Segment': tratto,
                'Length': LTratto,
                'L_Progr': Lprogressiva,
                'Qcd': Qcd,
                'Qcd_segment': Qcd_Tratto,
                'Tf': T,
                'Tmetal': Tp_Metallo,
                'Ti1': Tp1,
                'Ti2':Tp2,
                'Ts': Tp_Finitura
            })
                

        return Qcd_Tratto, Tfinale                 

    # Caso di tre strati di isolante termico
    if (numlayers == 3):
        Punto_Iniziale = 0
        Punto_Finale = 0
        Qcd_Tratto = 0.00
        # Inizializza la progress bar con valore 0
        #progress_bar = st.progress(0)
        progress_text = st.empty()

        for tratto in range(numTratti):
            # Calcola la percentuale di completamento
            
            percent_complete = (tratto+1)/(numTratti) * 100
            # Aggiorna la progress bar
            #progress_bar.progress(percent_complete)
            #progress_text.text(f"Progress: {tratto+1}/{numTratti} ({percent_complete}%)")
            progress_text.text(f"Progress: segment {tratto+1} of {numTratti} - ({percent_complete}%)")

            st.session_state.lprog = st.session_state.lprog + LTratto
           
            Ts = Ta
            Tp_Metallo = (T - Ta) * (thk + thki1 + thki2 + thki3 + thkFinish) / (thk + thki1 + thki2 + thki3 + thkFinish)
            Tp1 = (T - Ta) * (thki1 + thki2 +thki3 + thkFinish) / (thk + thki1 + thki2 + thki3 + thkFinish)
            Tp2 = (T - Ta) * (thki2 + thki3 + thkFinish) / (thk + thki1 + thki2 + thki3 + thkFinish)
            Tp3 = (T - Ta) * (thki3 + thkFinish) / (thk + thki1 + thki2 + thki3 + thkFinish)
            Tp_Finitura = (T - Ta) * (thkFinish) / (thk + thki1 + thki2 + thki3 + thkFinish)

            Port = P
            verifica = 1.5
            Qr = 0
            Qcv = 0
            Qcd = 0

            while not verifica <= 0:
                if T >= Ta:
                    Ts = Ts + delta_Ts
                elif T < Ta:
                    Ts = Ts-delta_Ts

                Qr =  Irraggiamento(T, Ta, Ts, e)
                Qcv = Convezione(T, Ta, Ts, W)
                Ae = (Qr + Qcv)

                temp_media = (T + Tp1) / 2
                # Trova K1
                codice_mat = codei1  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K1 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K1 = ', K1)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K2
                codice_mat = codei2  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K2 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K2 = ', K2)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K3
                codice_mat = codei3  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K3 = condIso_media
                K4 = 0
                K5 = 0
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K3 = ', K3)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                #    print("La variabile è una stringa.")
                #    print(condIso_media)
                #else:
                #    print(f"La conducibilità termica per {codice_mat} a {temp_media}°C è {condIso_media:.4f}")
                Qcd = Conduzione(numlayers, T, Ta, Ts, Cond_Tubo, OD, ID, K1, K2, K3, K4, K5, d1, d2, d3, d4, d5, condFinish, DFinish)   

                if T > Ta:

                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt2 = ((Qcd / pi) * ((1 / (2 * K2)) * (log((d2 / d1)))))
                    Dt3 = ((Qcd / pi) * ((1 / (2 * K3)) * (log((d3 / d2)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d3)))))

       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T - (Dt_Metallo)
                    Tp1 = T - (Dt_Metallo + Dt1)
                    Tp2 = T - (Dt_Metallo + Dt1 + Dt2)
                    Tp3 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3)
                    Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt_Finitura)
        
                else:        
                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt2 = ((Qcd / pi) * ((1 / (2 * K2)) * (log((d2 / d1)))))
                    Dt3 = ((Qcd / pi) * ((1 / (2 * K3)) * (log((d3 / d2)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d3)))))
       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp1 = T + (Dt_Metallo + Dt1)
                    Tp2 = T + (Dt_Metallo + Dt1 + Dt2)
                    Tp3 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3)
                    Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt_Finitura)


            # *****  Dal codice sopra esce qaundo 'verifica <= 0' ed esegue il codice sottostante ******
            # -----------------------------
            Qcd1 = Qcd
            Cal_Disp_Kcal = Qcd1 * 0.5898452
            Punto_Iniziale = Punto_Finale
            Punto_Finale = Punto_Iniziale + LTratto
            # valori inizio tratto
            Tiniziale = T
            Tf_precedente = st.session_state.TF
            TpMi = Tp_Metallo
            Tp1i = Tp1
            Tp2i = Tp2
            Tp3i = Tp3
            TpFi = Tp_Finitura

            if (section == 0 and tratto == 0):
                #st.session_state.lprog = 0
                st.session_state['output'] = [{
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': 0,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ti2': Tp2i,
                    'Ti3': Tp3i,
                    'Ts': TpFi
                }]
            # caso in cui per la sezione si inserisce una temperatura diversa dal tratto precednte
            if (section > 0 and tratto == 0 and Tiniziale != Tf_precedente):
                #st.session_state.lprog = 0
                st.session_state['output'].append ({
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': st.session_state.lprog - LTratto,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ti2': Tp2i,
                    'Ti3': Tp3i,
                    'Ts': TpFi
                })

            if T >= Ta :
                X2 = exp((-LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                # calcolo valori finali temperatura sulle varie interfacce
                #Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                #Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                #Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
       
                Tp_Metallo = T - (Dt_Metallo)
                Tp1 = T - (Dt_Metallo + Dt1)
                Tp2 = T - (Dt_Metallo + Dt1 + Dt2)
                Tp3 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3)
                Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt_Finitura)

                
            else:    
                X2 = exp((LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                 # calcolo valori finali temperatura sulle varie interfacce
                Tp1 = T + (Dt_Metallo + Dt1)
                Tp2 = T + (Dt_Metallo + Dt1 + Dt2)
                Tp3 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3)
                Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt_Finitura)

            valoreEstratto = float(K1)

            Lprogressiva = st.session_state.lprog
            print ('Tp1, TP2, Tp3, Dt_Finitura', Tp1, Tp2, Tp3, Dt_Finitura)

            st.session_state['output'].append({
            #    'ID': st.session_state.num_tratto-1,
                'Section': section,
                'Segment': tratto,
                'Length': LTratto,
                'L_Progr': Lprogressiva,
                'Qcd': Qcd,
                'Qcd_segment': Qcd_Tratto,
                'Tf': T,
                'Tmetal': Tp_Metallo,
                'Ti1': Tp1,
                'Ti2':Tp2,
                'Ti3':Tp3,
                'Ts': Tp_Finitura
            })
                

    
        return Qcd_Tratto, Tfinale                 
       
    # Caso di quattro strati di isolante termico
    if (numlayers == 4):
        Punto_Iniziale = 0
        Punto_Finale = 0
        Qcd_Tratto = 0.00
        # Inizializza la progress bar con valore 0
        #progress_bar = st.progress(0)
        progress_text = st.empty()

        for tratto in range(numTratti):
            # Calcola la percentuale di completamento
            
            percent_complete = (tratto+1)/(numTratti) * 100
            # Aggiorna la progress bar
            #progress_bar.progress(percent_complete)
            #progress_text.text(f"Progress: {tratto+1}/{numTratti} ({percent_complete}%)")
            progress_text.text(f"Progress: segment {tratto+1} of {numTratti} - ({percent_complete}%)")

            st.session_state.lprog = st.session_state.lprog + LTratto
           
            Ts = Ta
            Tp_Metallo = (T - Ta) * (thk + thki1 + thki2 + thki3 + thki4 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thkFinish)
            Tp1 = (T - Ta) * (thki1 + thki2 +thki3 + thki4 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thkFinish)
            Tp2 = (T - Ta) * (thki2 + thki3 + thki4 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thkFinish)
            Tp3 = (T - Ta) * (thki3 + thki4 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thkFinish)
            Tp4 = (T - Ta) * (thki4 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thkFinish)
            Tp_Finitura = (T - Ta) * (thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thkFinish)

            Port = P
            verifica = 1.5
            Qr = 0
            Qcv = 0
            Qcd = 0

            while not verifica <= 0:
                if T >= Ta:
                    Ts = Ts + delta_Ts
                elif T < Ta:
                    Ts = Ts-delta_Ts

                Qr =  Irraggiamento(T, Ta, Ts, e)
                Qcv = Convezione(T, Ta, Ts, W)
                Ae = (Qr + Qcv)

                temp_media = (T + Tp1) / 2
                # Trova K1
                codice_mat = codei1  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K1 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K1 = ', K1)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K2
                codice_mat = codei2  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K2 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K2 = ', K2)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K3
                codice_mat = codei3  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K3 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K3 = ', K3)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K4
                codice_mat = codei4  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K4 = condIso_media
                K5 = 0
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K4 = ', K4)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()

                #    print("La variabile è una stringa.")
                #    print(condIso_media)
                #else:
                #    print(f"La conducibilità termica per {codice_mat} a {temp_media}°C è {condIso_media:.4f}")
                Qcd = Conduzione(numlayers, T, Ta, Ts, Cond_Tubo, OD, ID, K1, K2, K3, K4, K5, d1, d2, d3, d4, d5, condFinish, DFinish)   

                if T > Ta:

                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt2 = ((Qcd / pi) * ((1 / (2 * K2)) * (log((d2 / d1)))))
                    Dt3 = ((Qcd / pi) * ((1 / (2 * K3)) * (log((d3 / d2)))))
                    Dt4 = ((Qcd / pi) * ((1 / (2 * K4)) * (log((d4 / d3)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d4)))))

       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T - (Dt_Metallo)
                    Tp1 = T - (Dt_Metallo + Dt1)
                    Tp2 = T - (Dt_Metallo + Dt1 + Dt2)
                    Tp3 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3)
                    Tp4 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4)
                    Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt_Finitura)
        
                else:        
                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt2 = ((Qcd / pi) * ((1 / (2 * K2)) * (log((d2 / d1)))))
                    Dt3 = ((Qcd / pi) * ((1 / (2 * K3)) * (log((d3 / d2)))))
                    Dt4 = ((Qcd / pi) * ((1 / (2 * K4)) * (log((d4 / d3)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d4)))))
       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp1 = T + (Dt_Metallo + Dt1)
                    Tp2 = T + (Dt_Metallo + Dt1 + Dt2)
                    Tp3 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3)
                    Tp4 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4)
                    Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt_Finitura)


            # *****  Dal codice sopra esce qaundo 'verifica <= 0' ed esegue il codice sottostante ******
            # -----------------------------
            Qcd1 = Qcd
            Cal_Disp_Kcal = Qcd1 * 0.5898452
            Punto_Iniziale = Punto_Finale
            Punto_Finale = Punto_Iniziale + LTratto
            # valori inizio tratto
            Tiniziale = T
            Tf_precedente = st.session_state.TF
            TpMi = Tp_Metallo
            Tp1i = Tp1
            Tp2i = Tp2
            Tp3i = Tp3
            Tp4i = Tp4
            TpFi = Tp_Finitura

            if (section == 0 and tratto == 0):
                #st.session_state.lprog = 0
                st.session_state['output'] = [{
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': 0,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ti2': Tp2i,
                    'Ti3': Tp3i,
                    'Ti4': Tp4i,
                    'Ts': TpFi
                }]
            # caso in cui per la sezione si inserisce una temperatura diversa dal tratto precednte
            if (section > 0 and tratto == 0 and Tiniziale != Tf_precedente):
                #st.session_state.lprog = 0
                st.session_state['output'].append ({
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': st.session_state.lprog - LTratto,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ti2': Tp2i,
                    'Ti3': Tp3i,
                    'Ti4': Tp4i,
                    'Ts': TpFi
                })

            if T >= Ta :
                X2 = exp((-LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                # calcolo valori finali temperatura sulle varie interfacce
                #Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                #Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                #Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
       
                Tp_Metallo = T - (Dt_Metallo)
                Tp1 = T - (Dt_Metallo + Dt1)
                Tp2 = T - (Dt_Metallo + Dt1 + Dt2)
                Tp3 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3)
                Tp4 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4)
                Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt_Finitura)

                
            else:    
                X2 = exp((LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                 # calcolo valori finali temperatura sulle varie interfacce
                Tp1 = T + (Dt_Metallo + Dt1)
                Tp2 = T + (Dt_Metallo + Dt1 + Dt2)
                Tp3 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3)
                Tp4 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4)
                Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt_Finitura)

            valoreEstratto = float(K1)

            Lprogressiva = st.session_state.lprog
            print ('Tp1, TP2, Tp3, Tp4, Dt_Finitura', Tp1, Tp2, Tp3, Tp4, Dt_Finitura)

            st.session_state['output'].append({
            #    'ID': st.session_state.num_tratto-1,
                'Section': section,
                'Segment': tratto,
                'Length': LTratto,
                'L_Progr': Lprogressiva,
                'Qcd': Qcd,
                'Qcd_segment': Qcd_Tratto,
                'Tf': T,
                'Tmetal': Tp_Metallo,
                'Ti1': Tp1,
                'Ti2':Tp2,
                'Ti3':Tp3,
                'Ti4':Tp4,
                'Ts': Tp_Finitura
            })
                
        return Qcd_Tratto, Tfinale                 
            
    # Caso di cinque strati di isolante termico
    if (numlayers == 5):
        Punto_Iniziale = 0
        Punto_Finale = 0
        Qcd_Tratto = 0.00
        # Inizializza la progress bar con valore 0
        #progress_bar = st.progress(0)
        progress_text = st.empty()

        for tratto in range(numTratti):
            # Calcola la percentuale di completamento
            
            percent_complete = (tratto+1)/(numTratti) * 100
            # Aggiorna la progress bar
            #progress_bar.progress(percent_complete)
            #progress_text.text(f"Progress: {tratto+1}/{numTratti} ({percent_complete}%)")
            progress_text.text(f"Progress: segment {tratto+1} of {numTratti} - ({percent_complete}%)")

            st.session_state.lprog = st.session_state.lprog + LTratto
           
            Ts = Ta
            Tp_Metallo = (T - Ta) * (thk + thki1 + thki2 + thki3 + thki4 + thki5 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thki5 + thkFinish)
            Tp1 = (T - Ta) * (thki1 + thki2 +thki3 + thki4 + thki5 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thki5 + thkFinish)
            Tp2 = (T - Ta) * (thki2 + thki3 + thki4 + thki5 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thki5 + thkFinish)
            Tp3 = (T - Ta) * (thki3 + thki4 + thki5 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thki5 + thkFinish)
            Tp4 = (T - Ta) * (thki4 + thki5 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thki5 + thkFinish)
            Tp5 = (T - Ta) * (thki5 + thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thki5 + thkFinish)
            Tp_Finitura = (T - Ta) * (thkFinish) / (thk + thki1 + thki2 + thki3 + thki4 + thki5 + thkFinish)

            Port = P
            verifica = 1.5
            Qr = 0
            Qcv = 0
            Qcd = 0

            while not verifica <= 0:
                if T >= Ta:
                    Ts = Ts + delta_Ts
                elif T < Ta:
                    Ts = Ts-delta_Ts

                Qr =  Irraggiamento(T, Ta, Ts, e)
                Qcv = Convezione(T, Ta, Ts, W)
                Ae = (Qr + Qcv)

                temp_media = (T + Tp1) / 2
                # Trova K1
                codice_mat = codei1  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K1 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K1 = ', K1)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K2
                codice_mat = codei2  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K2 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K2 = ', K2)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K3
                codice_mat = codei3  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K3 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K3 = ', K3)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K4
                codice_mat = codei4  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K4 = condIso_media
                K5 = 0
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K4 = ', K4)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()
                # Trova K5
                codice_mat = codei5  # codice materiale isolamento layer 1
                condIso_media = conducibilita_termica_interpolata(file_csv, codice_mat, temp_media)
                K5 = condIso_media
                if isinstance(condIso_media, str):
                    st.error('The isolant is not compatible with temperature. Please change it before proceed.')
                    st.write('K5 = ', K5)
                    #st.stop()
                    if st.button('Go back!'):
                        st.switch_page('pages/2_📉Temperature_Drop.py')
                    st.stop()

                #    print("La variabile è una stringa.")
                #    print(condIso_media)
                #else:
                #    print(f"La conducibilità termica per {codice_mat} a {temp_media}°C è {condIso_media:.4f}")
                Qcd = Conduzione(numlayers, T, Ta, Ts, Cond_Tubo, OD, ID, K1, K2, K3, K4, K5, d1, d2, d3, d4, d5, condFinish, DFinish)   

                if T > Ta:

                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt2 = ((Qcd / pi) * ((1 / (2 * K2)) * (log((d2 / d1)))))
                    Dt3 = ((Qcd / pi) * ((1 / (2 * K3)) * (log((d3 / d2)))))
                    Dt4 = ((Qcd / pi) * ((1 / (2 * K4)) * (log((d4 / d3)))))
                    Dt5 = ((Qcd / pi) * ((1 / (2 * K5)) * (log((d5 / d4)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d5)))))

       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp_Metallo = T - (Dt_Metallo)
                    Tp1 = T - (Dt_Metallo + Dt1)
                    Tp2 = T - (Dt_Metallo + Dt1 + Dt2)
                    Tp3 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3)
                    Tp4 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4)
                    Tp5 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt5)
                    Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt5 + Dt_Finitura)
        
                else:        
                    Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                    Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                    Dt2 = ((Qcd / pi) * ((1 / (2 * K2)) * (log((d2 / d1)))))
                    Dt3 = ((Qcd / pi) * ((1 / (2 * K3)) * (log((d3 / d2)))))
                    Dt4 = ((Qcd / pi) * ((1 / (2 * K4)) * (log((d4 / d3)))))
                    Dt5 = ((Qcd / pi) * ((1 / (2 * K5)) * (log((d5 / d4)))))
                    Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d5)))))
       
                    verifica = (Qcd) - (Ae * pi * (DFinish))
                    Tp1 = T + (Dt_Metallo + Dt1)
                    Tp2 = T + (Dt_Metallo + Dt1 + Dt2)
                    Tp3 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3)
                    Tp4 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4)
                    Tp5 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt5)
                    Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt5 + Dt_Finitura)


            # *****  Dal codice sopra esce qaundo 'verifica <= 0' ed esegue il codice sottostante ******
            # -----------------------------
            Qcd1 = Qcd
            Cal_Disp_Kcal = Qcd1 * 0.5898452
            Punto_Iniziale = Punto_Finale
            Punto_Finale = Punto_Iniziale + LTratto
            # valori inizio tratto
            Tiniziale = T
            Tf_precedente = st.session_state.TF
            TpMi = Tp_Metallo
            Tp1i = Tp1
            Tp2i = Tp2
            Tp3i = Tp3
            Tp4i = Tp4
            Tp5i = Tp5
            TpFi = Tp_Finitura

            if (section == 0 and tratto == 0):
                #st.session_state.lprog = 0
                st.session_state['output'] = [{
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': 0,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ti2': Tp2i,
                    'Ti3': Tp3i,
                    'Ti4': Tp4i,
                    'Ti5': Tp5i,
                    'Ts': TpFi
                }]
            # caso in cui per la sezione si inserisce una temperatura diversa dal tratto precednte
            if (section > 0 and tratto == 0 and Tiniziale != Tf_precedente):
                #st.session_state.lprog = 0
                st.session_state['output'].append ({
                    'Section': section,
                    'Segment': tratto,
                    'Length': 0,
                    'L_Progr': st.session_state.lprog - LTratto,
                    'Qcd': Qcd,
                    'Qcd_segment': Qcd_Tratto,
                    'Tf': Tiniziale,
                    'Tmetal': TpMi,
                    'Ti1': Tp1i,
                    'Ti2': Tp2i,
                    'Ti3': Tp3i,
                    'Ti4': Tp4i,
                    'Ti5': Tp5i,
                    'Ts': TpFi
                })

            if T >= Ta :
                X2 = exp((-LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                # calcolo valori finali temperatura sulle varie interfacce
                #Dt_Metallo = ((Qcd / pi) * ((1 / (2 * Cond_Tubo)) * (log((OD / ID)))))
                #Dt1 = ((Qcd / pi) * ((1 / (2 * K1)) * (log((d1 / OD)))))
                #Dt_Finitura = ((Qcd / pi) * ((1 / (2 * condFinish)) * (log((DFinish / d1)))))
       
                Tp_Metallo = T - (Dt_Metallo)
                Tp1 = T - (Dt_Metallo + Dt1)
                Tp2 = T - (Dt_Metallo + Dt1 + Dt2)
                Tp3 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3)
                Tp4 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4)
                Tp5 = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt5)
                Tp_Finitura = T - (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt5 + Dt_Finitura)

                
            else:    
                X2 = exp((LTratto / (Port * cal_spc)) * (Cal_Disp_Kcal / (T - Ta)))
                Tfinale = (T - Ta) * X2 + Ta
                T = Tfinale
                st.session_state.TF = Tfinale
                Qcd_Tratto = Qcd_Tratto + (Qcd * LTratto)

                 # calcolo valori finali temperatura sulle varie interfacce
                Tp1 = T + (Dt_Metallo + Dt1)
                Tp2 = T + (Dt_Metallo + Dt1 + Dt2)
                Tp3 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3)
                Tp4 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4)
                Tp5 = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt5)
                Tp_Finitura = T + (Dt_Metallo + Dt1 + Dt2 + Dt3 + Dt4 + Dt5 + Dt_Finitura)

            valoreEstratto = float(K1)

            Lprogressiva = st.session_state.lprog
            print ('Tp1, TP2, Tp3, Tp4, Tp5, Dt_Finitura', Tp1, Tp2, Tp3, Tp4, Tp5, Dt_Finitura)

            st.session_state['output'].append({
            #    'ID': st.session_state.num_tratto-1,
                'Section': section,
                'Segment': tratto,
                'Length': LTratto,
                'L_Progr': Lprogressiva,
                'Qcd': Qcd,
                'Qcd_segment': Qcd_Tratto,
                'Tf': T,
                'Tmetal': Tp_Metallo,
                'Ti1': Tp1,
                'Ti2':Tp2,
                'Ti3':Tp3,
                'Ti4':Tp4,
                'Ti5':Tp5,
                'Ts': Tp_Finitura
            })
                
        return Qcd_Tratto, Tfinale                 

        

                        






