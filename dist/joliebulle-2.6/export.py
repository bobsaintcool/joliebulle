#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.6
#Copyright (C) 2010-2012 Pierre Tavares

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.




import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import xml.etree.ElementTree as ET
from xml.dom import minidom



  

class Export (QtCore.QObject):

    
    
    def prettify(self,elem):

        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
        


    
    def exportXML(self,nomRecette, styleRecette, typeRecette, brewer, volume, boil, rendement, OG, FG, nbreHops, liste_houblons,
liste_hAmount, liste_hForm, liste_hTime, liste_hAlpha, liste_hUse, nbreFer, fNom, fAmount,
fType, fYield, fMashed, color, liste_ingr, liste_fAmount, liste_fType,
liste_fYield, liste_fMashed, liste_color, dNom, dAmount, dType, nbreDivers, liste_divers, liste_dAmount, liste_dType, liste_dTime, liste_dUse, nbreLevures, lNom, lForm, lLabo, lProd, lAtten, liste_levures, liste_lForm, liste_lLabo, liste_lProdid, liste_levureAtten, recipeNotes, mashProfile) :

        self.recipes = ET.Element('RECIPES')
        recipe = ET.SubElement(self.recipes, 'RECIPE')
        name = ET.SubElement(recipe, 'NAME')
        name.text = nomRecette
        version = ET.SubElement(recipe, 'VERSION')
        version.text = "1"
        type = ET.SubElement(recipe, 'TYPE')
        type.text = typeRecette
        brewerR = ET.SubElement(recipe, 'BREWER')
        brewerR.text = brewer
        
        
        style = ET.SubElement(recipe, 'STYLE')
        sNom = ET.SubElement(style, 'NAME')
        sNom.text = styleRecette
        sVersion = ET.SubElement(style, 'VERSION')
        sVersion.text = '1'
        sCategory = ET.SubElement(style, 'CATEGORY')
        sCategoryNumber = ET.SubElement (style, 'CATEGORY_NUMBER')
        sStyleLetter = ET.SubElement (style, 'STYLE_LETTER')
        sStyleGuide = ET.SubElement (style, 'STYLE_GUIDE')
        sType =ET.SubElement(style, 'TYPE')
        sType.text = 'Ale'
        sOgMin = ET.SubElement (style, 'OG_MIN')
        sOgMax = ET.SubElement (style, 'OG_MAX')
        sFgMin = ET.SubElement (style, 'FG_MIN')
        sFgMax = ET.SubElement (style, 'FG_MAX')
        sIbuMin = ET.SubElement (style, 'IBU_MIN')
        sIbuMax = ET.SubElement (style, 'IBU_MAX')
        sColorMin = ET.SubElement (style, 'COLOR_MIN')
        sColorMax = ET.SubElement (style, 'COLOR_MAX')
        
        
        batch_size = ET.SubElement(recipe, 'BATCH_SIZE')
        batch_size.text = str(volume)
        boil_size = ET.SubElement(recipe, 'BOIL_SIZE')
        boil_time = ET.SubElement(recipe, 'BOIL_TIME')
        boil_time.text = str(boil)
        efficiency = ET.SubElement(recipe, 'EFFICIENCY')
        efficiency.text = str(rendement)
        originalGravity = ET.SubElement(recipe, 'OG')
        originalGravity.text = str(OG)
        finalGravity = ET.SubElement(recipe, 'FG')
        finalGravity.text = str(FG)
        
        hops = ET.SubElement(recipe, 'HOPS')
        i=0
        while i < nbreHops :
            i = i+1
            hop = ET.SubElement(hops, 'HOP')
            hNom = ET.SubElement(hop, 'NAME')
            hVersion = ET.SubElement(hop, 'VERSION')
            hVersion.text = '1'
            hNom.text = liste_houblons[i-1]
            hAmount = ET.SubElement(hop, 'AMOUNT')
            hAmount.text = str(liste_hAmount[i-1]/1000)
            hForm = ET.SubElement(hop, 'FORM')
#            try :
            if str(liste_hForm[i-1]) == self.trUtf8('''Feuille''') :
                hForm.text = 'Leaf'
            if str(liste_hForm[i-1]) == self.trUtf8('''Pellet''') :
                hForm.text = 'Pellet'
            if str(liste_hForm[i-1]) == self.trUtf8('''Cône''') :
                hForm.text = 'Plug'   
#            except:
#                hForm.text = 'Leaf'

            print(self.trUtf8('''Feuille'''))
                
            hTime = ET.SubElement(hop, 'TIME')
            hTime.text = str(liste_hTime[i-1])
            hAlpha = ET.SubElement(hop, 'ALPHA')
            hAlpha.text = str(liste_hAlpha[i-1])
            hUse = ET.SubElement(hop, 'USE')
            try :
                if str(liste_hUse[i-1]) == self.trUtf8('''Ébullition''') :
                    hUse.text = 'Boil'
                if str(liste_hUse[i-1]) == self.trUtf8('Dry Hop') or str(liste_hUse[i-1]) == 'Dry Hopping' :
                    hUse.text = 'Dry Hop'  
                if str(liste_hUse[i-1]) == self.trUtf8('''Empâtage''') :
                    hUse.text = 'Mash'
                if str(liste_hUse[i-1]) == self.trUtf8('''Premier Moût''') :
                    hUse.text = 'First Wort' 
                if str(liste_hUse[i-1]) == self.trUtf8('''Arôme''') :
                    hUse.text = 'Aroma'  
            except :
                hUse.text = 'Boil'
            
            

        fermentables = ET.SubElement(recipe, 'FERMENTABLES')
        
        i = 0
        while i < nbreFer :
            i = i+1
            fermentable = ET.SubElement(fermentables, 'FERMENTABLE')
            fNom = ET.SubElement(fermentable,'NAME')
            fNom.text = liste_ingr[i-1]
            fVersion = ET.SubElement(fermentable, 'VERSION')
            fVersion.text = '1'            
            fAmount = ET.SubElement(fermentable, 'AMOUNT')
            fAmount.text = str(liste_fAmount[i-1]/1000)
            fType = ET.SubElement(fermentable, 'TYPE')
            fType.text = liste_fType[i-1]
            fYield = ET.SubElement(fermentable,'YIELD')
            fYield.text = str(liste_fYield[i-1])
            try:
                fMashed = ET.SubElement(fermentable,'RECOMMEND_MASH')
                if not liste_fMashed :
                    pass
                else :
                    fMashed.text = liste_fMashed[i-1]
            except :
                pass

            color = ET.SubElement(fermentable, 'COLOR')
            color.text = str(liste_color[i-1]/1.97)
            
        miscs = ET.SubElement(recipe, 'MISCS')
        i = 0
        while i < nbreDivers :
            i = i+1
            misc = ET.SubElement(miscs, 'MISC')
            dNom = ET.SubElement(misc, 'NAME')
            dNom.text = liste_divers[i-1]
            dVersion = ET.SubElement(misc, 'VERSION')
            dVersion.text = '1'
            dAmount = ET.SubElement(misc, 'AMOUNT')
            dAmount.text = str(liste_dAmount[i-1]/1000)
            dType = ET.SubElement(misc, 'TYPE')
            dType.text = liste_dType[i-1]
            dTime = ET.SubElement(misc, 'TIME')
            try :
                dTime.text = str(liste_dTime[i-1])
            except :
                dTime.text = str(0)
            dUse = ET.SubElement(misc, 'USE')
            try :
                if str(liste_dUse[i-1]) == self.trUtf8('''Ébullition''') : 
                    dUse.text = 'Boil'
                if str(liste_dUse[i-1]) == self.trUtf8('''Empâtage''') : 
                    dUse.text = 'Mash'
                if str(liste_dUse[i-1]) == self.trUtf8('''Primaire''') : 
                    dUse.text = 'Primary'        
                if str(liste_dUse[i-1]) == self.trUtf8('''Secondaire''') : 
                    dUse.text = 'Secondary'
                if str(liste_dUse[i-1]) == self.trUtf8('''Embouteillage''') : 
                    dUse.text = 'Bottling'       
            except :
                dUse.text = 'Boil'
        
        yeasts=ET.SubElement(recipe, 'YEASTS')  
        i = 0  
        while i < nbreLevures :
            i = i+1
            yeast = ET.SubElement(yeasts, 'YEAST')
            lNom = ET.SubElement(yeast, 'NAME')
            lVersion = ET.SubElement(yeast, 'VERSION')
            lVersion.text = '1'
            lType = ET.SubElement(yeast ,'TYPE')
            lType = 'Ale'
            lNom.text = liste_levures [i-1]
            try :
                lForm = ET.SubElement(yeast, 'FORM')
                lForm.text = liste_lForm[i-1]
            except :
                pass
            try :
                lLabo = ET.SubElement(yeast, 'LABORATORY')
                lLabo.text = liste_lLabo[i-1]
            except :
                pass
            try :
                lProd = ET.SubElement(yeast, 'PRODUCT_ID')
                lProd.text = liste_lProdid[i-1]
            except :
                pass
            lAtten = ET.SubElement(yeast, 'ATTENUATION')
            lAtten.text = str(liste_levureAtten[i-1])
            
        waters=ET.SubElement(recipe, 'WATERS')
        
        mash=ET.SubElement(recipe, 'MASH') 
        mName = ET.SubElement(mash, 'NAME')
        mName.text = mashProfile['name']
        mVersion = ET.SubElement(mash, 'VERSION')
        mVersion.text = '1'
        mGrainTemp = ET.SubElement(mash, 'GRAIN_TEMP')
        mGrainTemp.text = str(mashProfile['grainTemp'])
        mTunTemp = ET.SubElement(mash, 'TUN_TEMP')
        mTunTemp.text = str(mashProfile['tunTemp'])
        mSpargeTemp = ET.SubElement(mash, 'SPARGE_TEMP')
        mSpargeTemp.text = str(mashProfile['spargeTemp'])
        mPh = ET.SubElement(mash, 'PH')
        mPh.text = str(mashProfile['ph'])
        mSteps = ET.SubElement(mash, 'MASH_STEPS')
        
        listSteps = mashProfile['mashSteps']
        lenSteps = len(listSteps)
        i = 0
        while i < lenSteps :
            i = i+1
            mashStep =ET.SubElement(mSteps, 'MASH_STEP')           
            dicStep = listSteps[i-1]
            stepName = ET.SubElement(mashStep, 'NAME')
            stepName.text = dicStep['name']
            stepVersion = ET.SubElement(mashStep, 'VERSION')
            stepVersion.text = '1'
            stepType = ET.SubElement(mashStep, 'TYPE')
            stepType.text = dicStep['type']
            stepTime = ET.SubElement(mashStep, 'STEP_TIME')
            stepTime.text = str(dicStep['stepTime'])
            stepTemp = ET.SubElement(mashStep, 'STEP_TEMP')
            stepTemp.text = str(dicStep['stepTemp'])
            stepVol = ET.SubElement(mashStep, 'INFUSE_AMOUNT')
            stepVol.text = str(dicStep['stepVol'])
            
        
        
        
        try :
            notes = ET.SubElement(recipe, 'NOTES') 
            notes.text = recipeNotes   
        except :
            pass       
        
        #print (ET.tostring(recipes))
        #print (self.prettify(recipes))
        #ET.ElementTree(recipes).write(file=None)
        
        #self.enregistrer()
    def enregistrer(self,s) :
       # print (ET.tostring(self.recipes))
        
        ET.ElementTree(self.recipes).write(s,encoding="utf-8")
        

