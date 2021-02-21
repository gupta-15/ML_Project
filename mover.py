import os
import shutil
 
path = r'D:\Documents\Academics\semester VI\ES 654- ML\project\data'
path1 = r'D:\Documents\Academics\semester VI\ES 654- ML\project\renamed'
s = ['s1','s2','s4','s5','s6','s7','s8','s9','s10']
for person in s:
    temp = ['_downstairs_nowall_trial1','_downstairs_nowall_trial2','_downstairs_wall_trial1'
    ,'_downstairs_wall_trial2','_upstairs_nowall_trial1','_upstairs_nowall_trial2','_upstairs_wall_trial1'
    ,'_upstairs_wall_trial2']
    temp1 = ['_DS_N_T1','_DS_N_T2','_DS_W_T1','_DS_W_T2','_US_N_T1','_US_N_T2','_US_W_T1','_US_W_T2']
    for room in range(len(temp)):
        polar = ['A0_1_0','A1_1_45','A2_1_90','B0_3_0','B1_3_45','B2_3_90','C0_5_0','C1_5_45','C2_5_90']
        polar1 = ['_P0_D1.wav','_P1_D1.wav','_P2_D1.wav','_P0_D3.wav','_P1_D3.wav','_P2_D3.wav','_P0_D5.wav','_P1_D5.wav','_P2_D5.wav']
        for final in range(len(polar)):
            recording = [
            'recording0_0_1','recording0_0_2','recording0_0_3','recording0_0_4',
            'recording0_45_1','recording0_45_2','recording0_45_3','recording0_45_4',
            'recording0_90_1','recording0_90_2','recording0_90_3','recording0_90_4',
            'recording0_135_1','recording0_135_2','recording0_135_3','recording0_135_4',
            'recording0_180_1','recording0_180_2','recording0_180_3','recording0_180_4',
            'recording0_225_1','recording0_225_2','recording0_225_3','recording0_225_4',
            'recording0_270_1','recording0_270_2','recording0_270_3','recording0_270_4',
            'recording0_315_1','recording0_315_2','recording0_315_3','recording0_315_4',
            'recording1_0_1','recording1_0_2','recording1_0_3','recording1_0_4',
            'recording1_45_1','recording1_45_2','recording1_45_3','recording1_45_4',
            'recording1_90_1','recording1_90_2','recording1_90_3','recording1_90_4',
            'recording1_135_1','recording1_135_2','recording1_135_3','recording1_135_4',
            'recording1_180_1','recording1_180_2','recording1_180_3','recording1_180_4',
            'recording1_225_1','recording1_225_2','recording1_225_3','recording1_225_4',
            'recording1_270_1','recording1_270_2','recording1_270_3','recording1_270_4',
            'recording1_315_1','recording1_315_2','recording1_315_3','recording1_315_4']
            for record in recording:
                shutil.move(path+"\\"+person+"\\"+person+temp[room]+"\\"+polar[final]+"\\"+record+'_'+person+temp1[room]+polar1[final],path1)


#os.rename(path,'C:\Users\rkggp\OneDrive\Desktop\trial.txt')