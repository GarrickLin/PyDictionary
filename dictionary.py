#!/usr/bin/env python
#coding:utf-8
"""
  Author:  G.K.
  Purpose: 
  Created: 2016/3/3
"""

import sys
import json
import urllib2

"""
API key：779070219
keyfrom：GK-Blog
doctype: json
"""
api = u"http://fanyi.youdao.com/openapi.do?keyfrom=GK-Blog&key=779070219&type=data&doctype=json&version=1.1&q=".encode('utf-8')

somo = u"(ಥ_ಥ)"
bq = """
                          -@o      +}                       
                         #dM       BW                       
                        $#W        ha                       
                         W         ?)@                      
                       &W           W+}                     
                      8#v           ?#8                     
                     &m& +L#88m      8b                     
                   M%h          +    ~ZBM                   
           IamGK*                  +      @#&WIamGK         
            8  B                            8x   &          
         +  & M                            + (k o+          
            #                                  8&           
           W                       +            8           
        + 8          +                           W}         
         8  ~ &%%%B88fdb&W           d&&kW&B&[u+  %         
         #  M8 8            b % 8_                 B        
         #                                   %W #  M        
    B%   8~                                      Bo@        
       @8 &jm                                   W&+         
         @8 m  ~                               &W 8         
       %c     /MM                           j8   #          
   +             ~& #8&&8&8&#&M&#Wm#&&M&8*~      ]          
          ~          W8           M&                        
                   8 8     r]_     &#                       
                  #  &   #     M   *}8                      
                 *   8  8-      M   M o                     
                 8+ ML  M_#W%Mu+%   W B                     
                  W%&   qbbWBB/W    #0                      
                   818  kQoo%h8#   8                        
                                %&W                          
"""


def translate(word):
    t_api = api + urllib2.quote(word)
    out = ""
    try:
        content = urllib2.urlopen(t_api, timeout=3).read()
    except:
        #print "There might be a network problem.\nPlease try later!"
        out = somo + u" There might be a network problem.\nPlease try later!\n"
        out += bq
        return out
    try:
        content = json.loads(content)
        out = parse(content)
    except:
        #print "There might be an unhandled exception.\nPlease try later!"
        out = somo + u" There might be an unhandled exception.\nPlease try later!\n"
        out += bq        
    return out
    
def tryget(content, strs):
    cur = content
    for ss in strs:
        try:
            cur = cur[ss]
        except KeyError:
            return None
    return cur

def parse(content):
    code = content['errorCode']
    out = u""
    if code == 0: # Success
        u = tryget(content, ['basic', 'us-phonetic'])
        e = tryget(content, ['basic', 'uk-phonetic'])
        explains = tryget(content, ['basic', 'explains'])
        #print content['query'], ':', content['translation'][0]
        if content['query'] == content['translation'][0]:
            out += somo + u" Sorry, no translation result !\n"
            out += bq
        else:
            out += content['query']
            out += " : "
            out += content['translation'][0]
            out += "\n"
        if u is not None:
            out += "US: ["
            out += u
            out += "]   "            
        if e is not None:
            out += "UK: ["
            out += e
            out += "]\n"
        if explains is not None:            
            out += "----------------------------------------\n"
            out += '[Explains]\n'
            for i in range(len(explains)):                
                out += "   "
                out += explains[i]
                out += "\n"
        web = tryget(content, ['web'])
        if web is not None:
            out += "----------------------------------------\n"
            out += "[More..]\n"
            for eachweb in web:
                key = eachweb["key"]
                values = eachweb["value"]
                out += key + ": "
                for v in values:
                    out += v + ", "
                out = out[:-2]
                out += "\n"
    elif code == 20:
        #print "The Input is too long!"
        out += somo + u" The Input is too long!\n"
        out += bq
    elif code == 30:
        #print "Failed to translate!"
        out += somo + u" Failed to translate!\n"
        out += bq           
    elif code == 40:
        #print "Unsupported language!"
        out += somo + u" Unsupported language!\n"
        out += bq
    elif code == 50:
        #print "Unsupported input!"
        out += somo + u" Unsupported input!\n"
        out += bq
    elif code == 60:
        #print "Sorry, no translation result!"
        out += somo + u" Sorry, no translation result !\n"
        out += bq
    return out

if __name__ == "__main__":
    word = "smile"
    #pprint.pprint(word)
    translate(word)
