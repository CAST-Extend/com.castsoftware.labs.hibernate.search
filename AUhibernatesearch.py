'''
Created on DEC 25, 2017

@author: NNA
'''

import cast.analysers.jee
import cast.application
import cast.analysers.log as LOG
import os
from cast.analysers import Member,Bookmark
from setuptools.sandbox import _file
import xml.etree.ElementTree as ET
from Cython.Compiler.Options import annotate


def get_overriden(_type, member):
    """
    Get the ancestor's member this member overrides
    """
    member_name = member.get_name()
    
    result = []
    
    for parent in _type.get_inherited_types():
        
        for child in parent.get_children():
            if child.get_name() == member_name:
                result.append(child)
        
        result += get_overriden(parent, member)
        
    return result

class search(cast.analysers.jee.Extension):
    def __init__(self):
        self.result = None
        self.count = 1
        
        
               
    def start_analysis(self,options):
        LOG.debug('Successfully HIB Search analyzer Started')
        options.add_classpath('jars')
       
      
    def start_member(self, member):
        for anno in member.get_annotations():
            LOG.debug(str(anno))
            
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.Field)', member, 'HIBSEARCHFIELD')
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.Index)', member, 'HIBSEARCHINDEXED')
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.Analyze)', member, 'HIBSEARCHFIELD')
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.ContainedIn)', member, 'HIBSEARCHContainedIn')
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.IndexedEmbedded)', member, 'HIBSEARCHINDEXEMBEEDED')
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.Document)', member, 'HIBSEARCHDOCUMENT')
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.Boost)', member, 'HIBSEARCHBOOST')
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.Spatial)', member, 'HIBSEARCHSPATIAL')
            self.findannotation(anno, 'Type(org.hibernate.search.annotations.FieldBridge)', member, 'HIBSEARCHFieldBridge')
         
       
    # receive a java parser from platform
    @cast.Event('com.castsoftware.internal.platform', 'jee.java_parser')
    def receive_java_parser(self, parser):
        self.java_parser = parser
        LOG.debug('Successfully receive_java_parser')
        pass
        
    def findannotation(self, anno, annotext, member,val):
        if str(anno[0])== str(annotext):
            self.Createannsearch(member,anno[0],  annotext, val)
     
               
    def Createannsearch(self,typ,annoValue, annotext,val):
        annsearch = cast.analysers.CustomObject()
        annsearch.set_name(val)
        annsearch.set_type(val)
        parentFile = typ.get_position().get_file() 
        annsearch.set_parent(parentFile)
        annsearch.set_fullname(typ.get_fullname())  
        self.fielPath = parentFile.get_fullname()
        self.count= self.count+1
        annsearch.set_guid(self.fielPath+val +str(self.count))
        annsearch.save()
        annsearch.save_position(typ.get_position())
        cast.analysers.create_link('callLink', annsearch, typ )
        LOG.debug(annotext+  '   object is created with name '+ val)
        return self.Createannsearch; 
    
    
    def start_xml_file(self, file):
        LOG.debug('Scanning XML test file :' )
                       
    
                  
    
    def end_analysis(self):
        self.result
        
        #LOG.info("search Analyzer Analyzer Ended")
        
   
