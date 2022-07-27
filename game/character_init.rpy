# Character Objects for Ren'py
# --> Image is side image definition component
# --> Prefix and Suffix will add this to every dialogue uttered by character.

#
#   IMPORTANT CHARACTERS
#

#Main Character:
define character.fang = Character(__("Fang Jie"), image="fang", who_color="#3154b5", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="fang")

#Zhang Xiu Rong: Human Form
define character.zxr = Character(__("Zhang Xiu Rong"), image="zxr", what_prefix='"', what_suffix='"')

#Zhang Xiu Rong: Phoenix Form
define character.pho = Character(__("Phoenix"), image="pho", what_prefix='"', what_suffix='"')
# --> The soup of the story

#Prince Feng
define character.feng = Character(__("Feng Quan"), image="feng", what_prefix='"', what_suffix='"')

#Kismet: The Outsider Reborn
define character.kis = Character(__("Kismet"), image="kis", what_prefix='"', what_suffix='"')
#--> As an abstract entity his side image should be selected through random list to make him more entropic

#General Faral
define character.gnr = Character(__("General Faral - Placeholder"), image="gnr", what_prefix='"', what_suffix='"' )
#--> Name Discussion


#Fawang Ranni
define character.fwr = Character(__("Fawang Ranni"), image="fwr", what_prefix='"', what_suffix='"')

#River Goddess: Mazu
define character.maz = Character(__("Mazu"), image="maz", what_prefix='"', what_suffix='"')

#Phantom: The King of Shadows
define character.gui = Character(__("Phantom"), image="gui", what_prefix='"', what_suffix='"')

#Fei Yue: Maiden of the River
define character.fei = Character(__("Fei Yue"), image="fei", what_prefix='"', what_suffix='"')

#Lao Mu
define character.lao = Character(__("Lao Mu"), image="lao", what_prefix='"', what_suffix='"')

#Matsuyama Enshin
define character.mat = Character(__("Matsuyama Enshin"), image="mat", what_prefix='"', what_suffix='"')

#Son of the Wind
define character.sow = Character(__("Son of the Wind"),image="sow", what_prefix='"', what_suffix='"')