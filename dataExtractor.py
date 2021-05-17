import os
from typing import List, Dict
import pandas as pd
import numpy as np

class DataExtractor:
    """
    This class extracts data(measurement sequence) from a given path. the given path contains multiple text files.
    """

    def readDataFromDir(self, dirPath:str = None) -> Dict:
        """
        Reads data from the given directory path
        Input :
            dirPath(string) : path to directory which contains measurement data for GV maneuveur
        Output :
            result : dictionary containing processed dataframes
        """
        result ={
            'message':'',
            'files_processed': None,
            'processed_dataframes': None,
            'success': False
        }

        if dirPath == None or dirPath == '' :
            result['message'] = 'File path empty!!'
            return result

        if not os.path.exists(dirPath):
            result['message'] = 'File path doesnot exist!!'
            return result

        filesList = os.listdir(dirPath)
        if len(filesList) == 0:
            result['message'] = 'No files in directory!!'
            return result

        processedDataframes = []

        for file in filesList:
            df = pd.read_csv(dirPath+'/'+file, sep = '\t', engine = 'python', decimal = ',', skiprows=40)
            df = df.drop([0, 1])
            processedDataframes.append(df)

        result['message'] = 'Files successfully processed'
        result['files_processed'] = len(processedDataframes)
        result['processed_dataframes'] = processedDataframes
        result['success'] = True

        return result


    def processDataframeList(self, dataframeList:List = None):
        """
        Reads data from the given directory path
        Input :
            dirPath(string) : path to directory which contains measurement data for GV maneuveur
        Output :
            result : dictionary containing processed dataframes
        """
        required_features = [
                            'Lenkradwin', 'Lenkmoment', 'Fahrgeschw', 'Schwimmwin', 'Längsbesch', 'Querbeschl',
                           'Giergeschw', 'Nickwinkel', 'Wankwinkel', 'Gierwinkel', 'Nickgeschw', 'Wankgeschw',
                           'Hochbeschl', 'Fahrge_DIS', 'GPS_Status', 'Status_DIS', 'Status_TRK', 'GPS_FMS_St',
                           'Schwim_MSP', 'Schwim_MHA', 'Lichtschra', 'F_Spur_VL	F_Spur_VR', 'Radius	Fdiff_Spur',
                           'Längengrad', 'Breitengrd', 'Höhe', 'Fahrg_NULL', 'LenkgeschM', 'StWhl_Angl', 'StWhl_AnglSpd',
                           'VehSpd_Disp', 'Odo', 'AirTemp_Outsd_Disp', 'AirTemp_Outsd', 'BrkPdl_Stat', 'Brk_Stat', 'BrkTrq_V2',
                           'FullBrk_Actv', 'BrkIntrvntn_Actv_ESP', 'ESP_CtrlLmp_Info', 'VehAccel_X_V2', 'VehAccel_X_Offset',
                           'VehAccel_Y_V2', 'VehAccel_Y_Offset', 'VehYawRate_Raw', 'VehYawRateOffset_V2', 'WhlRPM_FL', 'WhlRPM_FR',
                           'WhlRPM_RL', 'WhlRPM_RR', 'AccelPdlPosn_Raw', 'AccelPdlPosn', 'KickDnSw_Psd', 'EngRPM', 'TankLvl',
                           'TankLvl_Disp_V2', 'SupBat_Volt', 'SupBat_Curr', 'StW_Trq_EPS', 'EPS_FtWhlAngl', 'EPS_FtWhlAngl_Offset'
                            ]

        pass


object = DataExtractor()
result = object.readDataFromDir("data/GV_1")
print(result['files_processed'])
print(result['message'])
print(result['success'])