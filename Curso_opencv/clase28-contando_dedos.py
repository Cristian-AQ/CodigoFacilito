import cv2
import numpy as np
import imutils

video = cv2.VideoCapture(0)

bg = None#fondo de la imagen

color_start = (204,204,0)
color_end = (204,0,204)
color_far = (255,0,0)

color_start_far = (204,204,0)
color_far_end = (204,0,204)
color_start_end = (0,255,255)

color_contorno = (0,255,0)
color_ymin = (0,130,255)#punto mas alto del contorno
color_angulo = (0,255,255)
color_d = (0,255,255)
color_fingers = (0,255,255)

while True:
    ret,frame = video.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        frame = imutils.resize(frame,width=640)
        frame_aux = frame.copy()
        if bg is not None:
            #cv2.imshow('V',bg)
            
            ROI = frame[50:300,380:600]#tomamos una region de interes
            cv2.rectangle(frame,(380-2,50+2),(600+2,300+2),color_fingers,1)#aparece cada vez q pongo i
            grayROI = cv2.cvtColor(ROI,cv2.COLOR_BGR2GRAY)

            bgROI = bg[50:300,380:600]
            #cv2.imshow('ROI',ROI)
            #cv2.imshow('grayROI',grayROI)
            #cv2.imshow('bgROI',bgROI)

            dif = cv2.absdiff(grayROI,bgROI)
            _,th = cv2.threshold(dif,30,255,cv2.THRESH_BINARY)
            th = cv2.medianBlur(th,7)
            #cv2.imshow('dif',dif)
            cv2.imshow('th',th)

            cnt,_ = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            cnt = sorted(cnt,key=cv2.contourArea,reverse=True)[:1]#ordenar de mayor a menor segun el area y obtener el mayor
            #cv2.drawContours(ROI,cnt,0,(0,255,0),2)

            for c in cnt:
                M = cv2.moments(c)
                if M['m00']==0:
                    M['m00'] = 1
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
                cv2.circle(ROI,(x,y),5,(0,255,0),-1)#dibujamos el centro del contorno

                ymin = c.min(axis=1)
                #ymin[0] xq en 0 se almacena las coordenadas donde esta presente ymin
                cv2.circle(ROI,tuple(ymin[0]),5,color_ymin,-1)

                hull1 = cv2.convexHull(c)
                cv2.drawContours(ROI,[hull1],0,color_contorno,2)

                hull2 = cv2.convexHull(c,returnPoints=False)
                defects = cv2.convexityDefects(c,hull2)

                if defects is not None:
                    inicio = []
                    fin = []
                    finger = 0
                    for i in range(defects.shape[0]):#desenpaquetar puntos
                        s,e,f,d = defects[i,0]
                        start = c[s][0]
                        end = c[e][0]
                        far = c[f][0]

                        if np.linalg.norm(start-end)>20 and d >12000:#ayuda a calcular la distancia entre dos puntos
                            inicio.append(start)
                            fin.append(end)
                            cv2.circle(ROI,tuple(start),5,color_start,2)#punto inicial(turquesa)
                            cv2.circle(ROI,tuple(end),5,color_end,2)#punto final(morado)
                            cv2.circle(ROI,tuple(far),7,color_far,-1)#punto mas alejado(azul)
                    if len(inicio)== 0:
                        minY = np.linalg.norm(ymin[0]-[x,y])
                        if minY >= 110:
                            finger = finger + 1
                            cv2.putText(ROI,f'{finger}',tuple(ymin[0]),1,1,color_fingers,1,cv2.LINE_AA)
                    
                    for i in range(len(inicio)):#es inicio xq hay la misma cantidad al inicio y final
                        finger = finger + 1
                        cv2.putText(ROI,f'{finger}',tuple(inicio[i]),1,1,color_fingers,1,cv2.LINE_AA)
                        if i == len(inicio)-1:
                            finger = finger + 1
                            cv2.putText(ROI,f'{finger}',tuple(fin[i]),1,1,color_fingers,1,cv2.LINE_AA)
                    
                    cv2.putText(frame,f'{finger}',(390,45),1,1,color_fingers,2,cv2.LINE_AA)

        
        cv2.imshow('A',frame)
        k = cv2.waitKey(1)
        
        if k == ord('i'):#realiza la captura del fondo 
            bg = cv2.cvtColor(frame_aux,cv2.COLOR_BGR2GRAY)
        
        if k == ord('x'):
            break

video.release()
cv2.destroyAllWindows()