import customtkinter as ctk

from script import coder, decoder

app = ctk.CTk()
app.title("")
app.geometry(geometry_string="875x600")
app.resizable(width=False, height=False)
ctk.set_appearance_mode(mode_string="light")

def crypt():
    
    dialog_for_crypt = ctk.CTkInputDialog(title="", text="Clé de chiffrement ?")
    
    try:
        encrypted_text = coder(text=input_txt.get(index1="0.0", index2="end"), key=dialog_for_crypt.get_input())
        output_txt.insert(index="0.0", text=encrypted_text)
    except:
        return None
    
def decrypt():
    
    dialog_for_decrypt = ctk.CTkInputDialog(title="", text="Clé de déchiffrement ?")
    
    try:
        decrypted_text = decoder(text=input_txt.get(index1="0.0", index2="end"), key=dialog_for_decrypt.get_input())
        output_txt.insert(index="0.0", text=decrypted_text)
    except:
        return None

def change_mode():

    if switch_mode.get() == "mode clair":
        ctk.set_appearance_mode(mode_string="light")
        switch_mode.configure(text="Thème clair")
        
    else:
        ctk.set_appearance_mode(mode_string="dark")
        switch_mode.configure(text="Thème sombre")


lbl_input_txt = ctk.CTkLabel(master=app, text="Texte à chiffrer/déchiffrer", )
lbl_input_txt.grid(column=0, row=0, pady=10)

lbl_output_txt = ctk.CTkLabel(master=app, text="Texte chiffré/déchiffré")
lbl_output_txt.grid(column=1, row=0, pady=10)

input_txt = ctk.CTkTextbox(master=app, width=420, height=500, wrap="word")
input_txt.grid(column=0, row=1, padx=10)

output_txt = ctk.CTkTextbox(master=app, width=420, height=500, wrap="word")
output_txt.grid(column=1, row=1, padx=5)

btn_to_crypt = ctk.CTkButton(master=app, text="Chiffrer", width=70, command=crypt)
btn_to_crypt.grid(column=0, row=2, ipadx=20, pady=10, padx=15, sticky="E")

btn_to_decrypt = ctk.CTkButton(master=app, text="Déchiffrer",width=70, command=decrypt)
btn_to_decrypt.grid(column=1, row=2, ipadx=20, pady=10, padx=15, sticky="W")

switch_mode = ctk.CTkSwitch(master=app, text="Thème clair", onvalue="mode sombre", offvalue="mode clair", command=change_mode)
switch_mode.grid(column=1, row=2, sticky="E")

app.mainloop()