import os,time,DWMManager,psutil
def DWMstate(answer):
    chkDWM = 'False'
    for process in psutil.process_iter():
        if process.name() == 'dwm.exe':
            chkDWM = 'True'
            break
    if not os.path.isfile(os.getcwd()+'\\pssuspend.exe'):
        print('경고\t\"pssuspend.exe\"파일을 같은 디렉토리에 넣으세요!!\n'*10)
        return 'ERROR'
    else:
        if answer == 'OFF' and chkDWM == 'True': #Disable
            time.sleep(0.5)
            os.chdir("C:\\Windows\\SystemApps\\Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy") #Disable StartMenuExperienceHost
            os.system('takeown /f StartMenuExperienceHost.exe')
            os.system('icacls StartMenuExperienceHost.exe /grant administrators:F')
            os.system('taskkill /f /im StartMenuExperienceHost.exe')
            os.system('rename StartMenuExperienceHost.exe StartMenuExperienceHost.exe.001')

            os.chdir("C:\\Windows\\SystemApps\\Microsoft.Windows.Search_cw5n1h2txyewy")    #Disable SearchApp
            os.system('takeown /f SearchApp.exe')
            os.system('icacls SearchApp.exe /grant administrators:F')
            os.system('taskkill /f /im SearchApp.exe')
            os.system('rename SearchApp.exe SearchApp.exe.001')

            os.system('taskkill /f /im TextInputHost.exe /im SearchApp.exe /im StartMenuExperienceHost.exe')

            os.chdir('C:\\Windows')
            os.system('takeown /f SystemApps')
            os.system('rename SystemApps SystemApps_')

            os.chdir(os.path.dirname(os.path.realpath(__file__)))
            os.system('pssuspend.exe winlogon.exe')
            os.system('taskkill /f /im dwm.exe')
            time.sleep(0.5)
        elif answer == 'ON' and chkDWM =='False':   #Enable
            time.sleep(0.5)
            os.chdir('C:\\Windows')
            os.system('takeown /f SystemApps')
            os.system('rename SystemApps_ SystemApps')

            os.chdir("C:\\Windows\\SystemApps\\Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy") #StartMenuExperienceHost.exe 파일 경로
            os.system('takeown /f StartMenuExperienceHost.exe.001') #Enable StartMenuExperienceHost
            os.system('icacls StartMenuExperienceHost.exe.001 /grant administrators:F')
            os.system('rename StartMenuExperienceHost.exe.001 StartMenuExperienceHost.exe')

            os.chdir("C:\\Windows\\SystemApps\\Microsoft.Windows.Search_cw5n1h2txyewy")    #Enable SearchApp
            os.system('takeown /f SearchApp.exe.001')
            os.system('icacls SearchApp.exe.001 /grant administrators:F')
            os.system('rename SearchApp.exe.001 SearchApp.exe')
            
            os.chdir(os.path.dirname(os.path.realpath(__file__)))
            os.system('pssuspend.exe -r winlogon.exe')
            time.sleep(0.5)
        else:
            return 'ERROR_DWM'
        return 'PASS'