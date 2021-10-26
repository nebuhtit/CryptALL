# CryptAnyL project # 15.04.21 Good version
#
from CryptAnyL_modules import *
import atexit

global driver
global pasw

try:
    os.mkdir(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with)
except FileExistsError:
    pass

def if_quit():
    # срабатывает когда программа выключаеться
    print('kek')
    try:
        f = open('setings.json', 'r', encoding='utf8')
        path_to_auto_open_file = json.load(f)['auto_open']
        f.close()

        os.remove(re.sub('.prcp', '', path_to_auto_open_file))
    except:
        print(traceback.format_exc())
        pass


atexit.register(if_quit)

try:

    from tkinter import *
    from tkinter import filedialog
    from subprocess import call
    from random import choice
    import json




    # COLORS

    colors = ['#F9EBEA', '#FDEDEC', '#F5EEF8', '#F4ECF7', '#EAF2F8', '#EBF5FB', '#E8F8F5', '#E8F6F3', '#E9F7EF', '#EAFAF1', '#FEF9E7', '#FEF5E7', '#FBEEE6', '#F8F9F9', '#FEFDE7', '#FAFEE7', '#F5FEE7', '#E7FEF4', '#E7FEF8', '#E7E9FE', '#FEE7FB', '#F2F4F4']




    def Enter_Entery_password(event=None):

        try:
            try:
                pasw = first_password
            except:
                pasw = Entry_password.get()
            privatkey = dec_F_import(pasw, 'personalresAA.txt')
            try:

                # основная часть, которая появляеться после правильного ввода пароля.

                INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
                print('there is all keys')
                root.destroy()
                root_work = Tk()
                root_work.title("CryptAL")
                root_work.configure(bg='white')
                x = (root_work.winfo_screenwidth() - root_work.winfo_reqwidth()) / 2
                y = (root_work.winfo_screenheight() - root_work.winfo_reqheight()) / 2
                root_work.wm_geometry("+%d+%d" % (x, y))

                frame_1 = Frame(root_work)
                frame_1.grid(column=0, row=3)

                Button_encrypt_file = Button(frame_1, text='encrypt file')
                Button_encrypt_file.grid(column=0, row=2, padx="6", pady="6")

                Entry_encrypt_file = Entry(frame_1, bg='#F8F8F8', width=28 )
                Entry_encrypt_file.grid(column=1, row=2, padx="6", pady="6")

                Entry_encrypt_file.configure(state=DISABLED)

                Button_decrypt_file = Button(frame_1, text='decrypt file')
                Button_decrypt_file.grid(column=0, row=3, padx="6", pady="6")

                Entry_decrypt_file = Entry(frame_1, bg='#F8F8F8', width=28)
                Entry_decrypt_file.grid(column=1, row=3, padx="6", pady="6")
                Entry_decrypt_file.configure(state=DISABLED)

                # Encrypting file

                def open_file(event=None):
                    global pathh
                    Tk().withdraw()
                    pathh = askopenfilename(title="Select file")

                    Entry_encrypt_file.configure(state=NORMAL)
                    Entry_encrypt_file.insert(0, 'Create password for file')
                    Entry_encrypt_file.focus_force()
                    Entry_decrypt_file.configure(state=DISABLED)
                    Button_decrypt_file.configure(state=DISABLED)
                    Button_encrypt_file.configure(state=DISABLED)

                Button_encrypt_file.bind('<Button-1>', open_file)

                def enrypt_file_by_passw(event=None):
                    pasww = Entry_encrypt_file.get()
                    encF_byPass(pathh, pasww)
                    Entry_encrypt_file.delete(0, 'end')
                    Entry_encrypt_file.configure(state=DISABLED)
                    Entry_decrypt_file.configure(state=DISABLED)
                    Button_decrypt_file.configure(state=NORMAL)
                    Button_encrypt_file.configure(state=NORMAL)

                def clear_Entry_encrypt(event=None):
                    if Entry_encrypt_file.get() == 'Create password for file':
                        Entry_encrypt_file.delete(0, 'end')

                Entry_encrypt_file.bind('<Key>', clear_Entry_encrypt)
                Entry_encrypt_file.bind('<Button-1>', clear_Entry_encrypt)
                Entry_encrypt_file.bind('<Return>', enrypt_file_by_passw)

                # Decrypting file

                def open_file_for_decrypt(event=None):
                    global pathh2
                    Tk().withdraw()
                    pathh2 = askopenfilename(title="Select file")

                    Entry_decrypt_file.configure(state=NORMAL)
                    Entry_decrypt_file.insert(0, 'Enter password for file')
                    Entry_decrypt_file.focus_force()
                    Entry_encrypt_file.configure(state=DISABLED)
                    Button_encrypt_file.configure(state=DISABLED)
                    Button_decrypt_file.configure(state=DISABLED)

                Button_decrypt_file.bind('<Button-1>', open_file_for_decrypt)

                def derypt_file_by_passw(event=None):
                    pasww = Entry_decrypt_file.get()
                    try:
                        decF_byPass(pathh2, pasww)
                        Entry_decrypt_file.delete(0, 'end')
                        Entry_decrypt_file.configure(bg='LightGreen')
                        Entry_decrypt_file.configure(state=DISABLED)
                        targetDirectory = os.path.dirname(str("CryptALL/" + who_do_u_want_to_chat_with +'/Collection/'+re.sub(r'.prcp', '', os.path.basename(pathh2))))
                        call(["open", targetDirectory])


                    except:
                        print(traceback.format_exc())
                        Entry_decrypt_file.delete(0, 'end')
                        Entry_decrypt_file.configure(bg='LightPink')
                        pass

                    Entry_encrypt_file.configure(state=NORMAL)
                    Button_encrypt_file.configure(state=NORMAL)
                    Button_decrypt_file.configure(state=NORMAL)

                def clear_Entry_decrypt(event=None):
                    if Entry_decrypt_file.get() == 'Enter password for file':
                        Entry_decrypt_file.delete(0, 'end')
                        Entry_decrypt_file.configure(show='●')
                    if Entry_decrypt_file.get() == '':
                        Entry_decrypt_file.configure(bg='white')

                Entry_decrypt_file.bind('<Key>', clear_Entry_decrypt)
                Entry_decrypt_file.bind('<Button-1>', clear_Entry_decrypt)
                Entry_decrypt_file.bind('<Return>', derypt_file_by_passw)


                # Отправка писем и файлов

                frame_2 = Frame(root_work)
                frame_2.grid(column=0, row=4)

                Button_sent_file = Button(frame_2, text='Sent file')
                Button_sent_file.grid(column=0, row=0)

                Text_write_massage = Text(frame_2, height=5, width=52, bg='#F5F5F5')
                Text_write_massage.grid(column=0, row=1)
                Text_write_massage.insert(1.0, 'Write a message')
                Text_write_massage.focus_force()



                def insert_Text_write_massage(event=None):
                    if Text_write_massage.get(1.0, "end-1c") == '':
                        Text_write_massage.insert(1.0, 'Write a message')
                Text_write_massage.bind('<FocusOut>', insert_Text_write_massage)

                def clear_Text_write_massage(event=None):
                    if Text_write_massage.get(1.0, "end-1c") == 'Write a message':
                        Text_write_massage.delete(1.0, END)
                Text_write_massage.bind('<FocusIn>', clear_Text_write_massage)


                # Отправка письма, Прием писем и файлов

                frame_3 = Frame(root_work)
                frame_3.grid(column=0, row=5)

                Text_your_encrypted_m = Text(frame_3, height=11, width=30, bg=choice(colors), font="Arial 9")
                Text_your_encrypted_m.grid(column=0, row=0)
                Text_your_encrypted_m.insert(1.0, 'Your encrypted message will be here, \nsend it\n'
                                                  'Double-Lсlick for copy\n\n'
                                                  'Здесь будет ваше зашиф. сообщение \nотправьте его\n2ЛКМ что бы скопировать\n\n')

                Text_friends_encr_massage = Text(frame_3, height=11, width=30, bg=choice(colors), font="Arial 9")
                Text_friends_encr_massage.grid(column=1, row=0)
                Text_friends_encr_massage.insert(1.0, "Paste your friend's encrypted message here\n"
                                                      "Double-Lсlick for past\n\n"
                                                      "Вставте сюда зашиф. сообщение вашего друга\n"
                                                      "2ЛКМ для вставки\n")




                def clear_Text_friends_encr_massage(event=None):
                    if Text_friends_encr_massage.get(1.0, "end-1c") == ("Paste your friend's encrypted message here\n"
                                                      "Double-Lсlick for past\n\n"
                                                      "Вставте сюда зашиф. сообщение вашего друга\n"
                                                      "2ЛКМ для вставки\n"):
                        Text_friends_encr_massage.delete(1.0, END)

                Text_friends_encr_massage.bind('<FocusIn>', clear_Text_friends_encr_massage)




                Button_receive_file = Button(frame_3, text='Receive file')
                Button_receive_file.grid(column=1, row=1)

                def Receive_File(event=None):
                    global pathh5
                    Tk().withdraw()
                    pathh5 = askopenfilename(title="Select file")
                    defile(pathh5, pasw)
                    targetDirectory = os.path.dirname(
                        str("CryptALL/" + who_do_u_want_to_chat_with + '/Down_files/' + re.sub(r'.prcp', '', os.path.basename(pathh5))))
                    print(targetDirectory)
                    call(["open", targetDirectory])

                Button_receive_file.bind('<Button-1>', Receive_File)

                # Переписка

                frame_4 = Frame(root_work)
                frame_4.grid(column=0, row=6)

                Text_correspondence = Text(frame_4, width=51, bg=choice(colors))
                Text_correspondence.grid(column=0, row=0)

                # # Auto open file
                #
                # frame_6 = Frame(root_work)
                # frame_6.grid(column=0, row=7)
                #
                # Button_auto_open = Button(frame_6, text='Auto open file')
                # Button_auto_open.grid(column=0, row=0)
                #
                # Button_delete_all_data = Button(frame_6, text='delete all data')
                # Button_delete_all_data.grid(column=1, row=0)
                #
                # def delete_all_data(event=None):
                #
                #
                #     root_alert = Tk()
                #     root_alert.title("Are you sure?")
                #     Yes = Button(root_alert, text='Yes')
                #     Yes.grid(column=0, row=0)
                #     No = Button(root_alert, text='No')
                #     No.grid(column=2, row=0)
                #
                #     def delete_all_YES_DANGEROUS(event=None):
                #         with open('delete.txt', 'w') as f:
                #             f.write('')
                #         print(os.path.dirname('delete.txt'))
                #         targetDirectory = os.getcwd()
                #         os.remove(targetDirectory+'Collection')
                #
                #     Yes.bind('<Button-1>', delete_all_YES_DANGEROUS)
                #
                #     def delete_all_NO(event=None):
                #         root_alert.destroy()
                #
                #     No.bind('<Button-1>', delete_all_NO)
                #
                #
                #
                # Button_delete_all_data.bind('<Button-1>', delete_all_data)
                #
                #
                # def check_auto_open(event=None):
                #     try:
                #         f = open('setings.json', 'r', encoding='utf8')
                #         path_to_auto_open_file = json.load(f)['auto_open']
                #         f.close()
                #         decF_byPass(path_to_auto_open_file, pasw)
                #         targetDirectory = os.path.dirname(
                #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(path_to_auto_open_file))))
                #
                #         Button_auto_open.configure(text='clear auto open file')
                #
                #         call(["open", targetDirectory])
                #
                #
                #     except:
                #         print(traceback.format_exc())
                #         pass
                # check_auto_open()
                #
                #
                # def auto_open_button(event=None):
                #     try:
                #         f = open('setings.json', 'r', encoding='utf8')
                #         d = json.load(f)
                #         Tk().withdraw()
                #         path_to_auto_open_file = d['auto_open']
                #         os.remove(re.sub('.prcp', '', path_to_auto_open_file))
                #         os.remove( path_to_auto_open_file)
                #         pathh7 = askopenfilename(title="Select file")
                #         encF_byPass(pathh7, pasw)
                #         Directory, Subject = os.path.split(pathh7)
                #
                #         targetDirectory = os.path.dirname(
                #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(pathh7))))
                #         encrypted_file_dir = targetDirectory +'/'+  os.path.basename(Subject)+'.prcp'
                #
                #         d.update({'auto_open': encrypted_file_dir})
                #         f.close()
                #         F = open('setings.json', 'w', encoding='utf8')
                #         json.dump(d, F, indent=4)
                #         F.close()
                #     except:
                #         Tk().withdraw()
                #         pathh6 = askopenfilename(title="Select file")
                #         encF_byPass(pathh6, pasw)
                #         Directory, Subject = os.path.split(pathh6)
                #         targetDirectory = os.path.dirname(
                #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(pathh6))))
                #         encrypted_file_dir = targetDirectory +'/'+ os.path.basename(Subject)+'.prcp'
                #         d = {'auto_open': encrypted_file_dir, 'style': 'none'}
                #         with open('setings.json', 'w', encoding='utf8') as f:
                #             json.dump(d, f, indent=4)
                #         Button_auto_open.configure(text='clear auto open file')
                # Button_auto_open.bind('<Button-1>', auto_open_button)




                # Function

                def Sent_File(event=None):
                    global pathh4
                    Tk().withdraw()
                    pathh4 = askopenfilename(title="Select file")
                    enfile(pathh4, pasw)
                    targetDirectory = os.path.dirname(
                        str("CryptALL/"  + who_do_u_want_to_chat_with + '/For_sent/' + re.sub(r'.prcp', '', os.path.basename(pathh4))))
                    call(["open", targetDirectory])
                    Text_correspondence.insert(1.0, 'In the opened window, an encrypted file, send it\nВ открывшемся окне заш. файл, отправьте его\n\n')

                Button_sent_file.bind('<Button-1>', Sent_File)

                def Encrypt_Message(event=None):
                    global myEncryptM
                    INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
                    message = Text_write_massage.get(1.0, "end-1c")
                    INP_Fkeys = b64out(INP_Fkeys)
                    # print("INP_Fkeys:", INP_Fkeys)
                    myEncryptM = en(message, INP_Fkeys)
                    INP_Fkeys = b64in(INP_Fkeys)

                    Text_your_encrypted_m.delete(1.0, END)
                    Text_your_encrypted_m.insert(1.0, myEncryptM)

                    Text_correspondence.insert(1.0, str("Me: " + message + "\n\n"))

                Text_write_massage.bind('<Return>', Encrypt_Message)

                def Decrypt_Friends_Message(event=None):
                    INP_Fmessage = Text_friends_encr_massage.get(1.0, "end-1c")
                    INP_Fmessage = re.sub(r'\s+', '', INP_Fmessage)
                    try:
                        F_encrypted_m = de(INP_Fmessage, privatkey)
                    except:
                        print(":(")
                    Text_correspondence.insert(1.0, str(" - " + F_encrypted_m + "\n\n"))

                Text_friends_encr_massage.bind('<Return>', Decrypt_Friends_Message)

                def double_click_Text_your_encrypted_m(event=None):
                    global clipboard_action
                    root_work.clipboard_clear()
                    clipboard_action = root_work.clipboard_append(myEncryptM)

                    # Text_your_encrypted_m.insert(1.0, "COPIED\n")
                Text_your_encrypted_m.bind('<Double-Button-1>', double_click_Text_your_encrypted_m)

                def double_click_Text_friends_encr_massage(event=None):
                    Text_friends_encr_massage.delete(1.0, END)
                    Text_friends_encr_massage.delete(0.0, END)
                    Text_friends_encr_massage.insert(1.0, root_work.clipboard_get())
                    Decrypt_Friends_Message()

                Text_friends_encr_massage.bind('<Double-Button-1>', double_click_Text_friends_encr_massage)





            except:
                root.destroy()
                root_main = Tk()
                root_main.title("CryptAL")
                root_main.configure(bg='white')
                x = (root_main.winfo_screenwidth() - root_main.winfo_reqwidth()) / 2
                y = (root_main.winfo_screenheight() - root_main.winfo_reqheight()) / 2
                root_main.wm_geometry("+%d+%d" % (x, y))

                pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
                Text_Main = Text(root_main, height=15)
                Text_Main.insert(0.0, str('Your public key:\n' + str(pubkeyFromFile) + '\nsent it to your friend\nDouble Click for COPY'))
                Text_Main.grid(column=0, row=0)
                Text_Main.focus_force()

                def clear_Text_Main(event=None):
                    Text_Main.delete(0.0, END)
                    Text_Main.insert(0.0, pubkeyFromFile)


                def inser_Text_Main(event=None):
                    Text_Main.delete(0.0, END)
                    Text_Main.insert(0.0, str('Your public key:\n' + str(pubkeyFromFile) + '\nsent it to your friend\nDouble Click for COPY'))

                def doubleClick_copy_Text_Main(event=None):
                    root_main.clipboard_clear()
                    root_main.clipboard_append(pubkeyFromFile)
                    Text_Main.delete(0.0, END)
                    Text_Main.insert(0.0, 'COPIED')

                Text_Main.bind('<Button-1>', clear_Text_Main)
                Text_Main.bind('<FocusIn>', clear_Text_Main)
                Text_Main.bind('<FocusOut>', inser_Text_Main)
                Text_Main.bind('<Double-Button-1>', doubleClick_copy_Text_Main)

                Text_Friends_key = Text(root_main, height=14)
                Text_Friends_key.grid(column=0, row=1, padx="6", pady="6")
                Text_Friends_key.focus_force()

                def clear_Friends_key(event=None):
                    Text_Friends_key.delete(0.0, END)

                def inser_Friends_key(event=None):
                    Text_Friends_key.insert(0.0, "Past Friend's key")

                def past_inser_Friends_key(event=None):
                    Text_Friends_key.insert(0.0, root_main.clipboard_get())

                Text_Friends_key.bind('<Double-Button-1>', past_inser_Friends_key)

                Text_Friends_key.bind('<Button-1>', clear_Friends_key)
                Text_Friends_key.bind('<FocusIn>', clear_Friends_key)

                Text_Friends_key.bind('<FocusOut>', inser_Friends_key)

                def past_inser_Friends_key(event=None):
                    Text_Friends_key.insert(0.0, root_main.clipboard_get())

                Text_Friends_key.bind('<Double-Button-1>', past_inser_Friends_key)


                def past_Friens_key(event=None):
                    INP_Fkeys = re.sub(r'\s', '', Text_Friends_key.get("1.0", END))
                    enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
                    privatkey = dec_F_import(pasw, 'personalresAA.txt')
                    print('friends key saved')
                    Text_Friends_key.delete(1.0, 'end')
                    Text_Friends_key.insert(1.0, 'friends key saved')
                    root_main.destroy()
                    root_work = Tk()
                    root_work.title("CryptAL")
                    root_work.configure(bg='white')
                    x = (root_work.winfo_screenwidth() - root_work.winfo_reqwidth()) / 2
                    y = (root_work.winfo_screenheight() - root_work.winfo_reqheight()) / 2
                    root_work.wm_geometry("+%d+%d" % (x, y))

                    frame_1 = Frame(root_work)
                    frame_1.grid(column=0, row=3)

                    Button_encrypt_file = Button(frame_1, text='encrypt file')
                    Button_encrypt_file.grid(column=0, row=2, padx="6", pady="6")

                    Entry_encrypt_file = Entry(frame_1, bg='#F8F8F8', width=28)
                    Entry_encrypt_file.grid(column=1, row=2, padx="6", pady="6")

                    Entry_encrypt_file.configure(state=DISABLED)

                    Button_decrypt_file = Button(frame_1, text='decrypt file')
                    Button_decrypt_file.grid(column=0, row=3, padx="6", pady="6")

                    Entry_decrypt_file = Entry(frame_1, bg='#F8F8F8', width=28)
                    Entry_decrypt_file.grid(column=1, row=3, padx="6", pady="6")
                    Entry_decrypt_file.configure(state=DISABLED)

                    # Encrypting file

                    def open_file(event=None):
                        global pathh
                        Tk().withdraw()
                        pathh = askopenfilename(title="Select file")

                        Entry_encrypt_file.configure(state=NORMAL)
                        Entry_encrypt_file.insert(0, 'Create password for file')
                        Entry_encrypt_file.focus_force()
                        Entry_decrypt_file.configure(state=DISABLED)
                        Button_decrypt_file.configure(state=DISABLED)
                        Button_encrypt_file.configure(state=DISABLED)

                    Button_encrypt_file.bind('<Button-1>', open_file)

                    def enrypt_file_by_passw(event=None):
                        pasww = Entry_encrypt_file.get()
                        encF_byPass(pathh, pasww)
                        Entry_encrypt_file.delete(0, 'end')
                        Entry_encrypt_file.configure(state=DISABLED)
                        Entry_decrypt_file.configure(state=DISABLED)
                        Button_decrypt_file.configure(state=NORMAL)
                        Button_encrypt_file.configure(state=NORMAL)

                    def clear_Entry_encrypt(event=None):
                        if Entry_encrypt_file.get() == 'Create password for file':
                            Entry_encrypt_file.delete(0, 'end')

                    Entry_encrypt_file.bind('<Key>', clear_Entry_encrypt)
                    Entry_encrypt_file.bind('<Button-1>', clear_Entry_encrypt)
                    Entry_encrypt_file.bind('<Return>', enrypt_file_by_passw)

                    # Decrypting file

                    def open_file_for_decrypt(event=None):
                        global pathh2
                        Tk().withdraw()
                        pathh2 = askopenfilename(title="Select file")

                        Entry_decrypt_file.configure(state=NORMAL)
                        Entry_decrypt_file.insert(0, 'Enter password for file')
                        Entry_decrypt_file.focus_force()
                        Entry_encrypt_file.configure(state=DISABLED)
                        Button_encrypt_file.configure(state=DISABLED)
                        Button_decrypt_file.configure(state=DISABLED)

                    Button_decrypt_file.bind('<Button-1>', open_file_for_decrypt)

                    def derypt_file_by_passw(event=None):
                        pasww = Entry_decrypt_file.get()
                        try:
                            decF_byPass(pathh2, pasww)
                            Entry_decrypt_file.delete(0, 'end')
                            Entry_decrypt_file.configure(bg='LightGreen')
                            Entry_decrypt_file.configure(state=DISABLED)
                            targetDirectory = os.path.dirname(
                                str("CryptALL/" + who_do_u_want_to_chat_with + '/Collection/' + re.sub(r'.prcp', '', os.path.basename(pathh2))))
                            call(["open", targetDirectory])


                        except:
                            print(traceback.format_exc())
                            Entry_decrypt_file.delete(0, 'end')
                            Entry_decrypt_file.configure(bg='LightPink')
                            pass

                        Entry_encrypt_file.configure(state=NORMAL)
                        Button_encrypt_file.configure(state=NORMAL)
                        Button_decrypt_file.configure(state=NORMAL)

                    def clear_Entry_decrypt(event=None):
                        if Entry_decrypt_file.get() == 'Enter password for file':
                            Entry_decrypt_file.delete(0, 'end')
                            Entry_decrypt_file.configure(show='●')
                        if Entry_decrypt_file.get() == '':
                            Entry_decrypt_file.configure(bg='white')

                    Entry_decrypt_file.bind('<Key>', clear_Entry_decrypt)
                    Entry_decrypt_file.bind('<Button-1>', clear_Entry_decrypt)
                    Entry_decrypt_file.bind('<Return>', derypt_file_by_passw)

                    # Отправка писем и файлов

                    frame_2 = Frame(root_work)
                    frame_2.grid(column=0, row=4)

                    Button_sent_file = Button(frame_2, text='Sent file')
                    Button_sent_file.grid(column=0, row=0)

                    Text_write_massage = Text(frame_2, height=5, width=52, bg='#F5F5F5')
                    Text_write_massage.grid(column=0, row=1)
                    Text_write_massage.insert(1.0, 'Write a message')
                    Text_write_massage.focus_force()

                    def insert_Text_write_massage(event=None):
                        if Text_write_massage.get(1.0, "end-1c") == '':
                            Text_write_massage.insert(1.0, 'Write a message')

                    Text_write_massage.bind('<FocusOut>', insert_Text_write_massage)

                    def clear_Text_write_massage(event=None):
                        if Text_write_massage.get(1.0, "end-1c") == 'Write a message':
                            Text_write_massage.delete(1.0, END)

                    Text_write_massage.bind('<FocusIn>', clear_Text_write_massage)

                    # Отправка письма, Прием писем и файлов

                    frame_3 = Frame(root_work)
                    frame_3.grid(column=0, row=5)

                    Text_your_encrypted_m = Text(frame_3, height=11, width=30, bg=choice(colors), font="Arial 9")
                    Text_your_encrypted_m.grid(column=0, row=0)
                    Text_your_encrypted_m.insert(1.0, 'Your encrypted message will be here, \nsend it\n'
                                                      'Double-Lсlick for copy\n\n'
                                                      'Здесь будет ваше зашиф. сообщение \nотправьте его\n2ЛКМ что бы скопировать\n\n')

                    Text_friends_encr_massage = Text(frame_3, height=11, width=30, bg=choice(colors), font="Arial 9")
                    Text_friends_encr_massage.grid(column=1, row=0)
                    Text_friends_encr_massage.insert(1.0, "Paste your friend's encrypted message here\n"
                                                          "Double-Lсlick for past\n\n"
                                                          "Вставте сюда зашиф. сообщение вашего друга\n"
                                                          "2ЛКМ для вставки\n")

                    def clear_Text_friends_encr_massage(event=None):
                        if Text_friends_encr_massage.get(1.0, "end-1c") == (
                        "Paste your friend's encrypted message here\n"
                        "Double-Lсlick for past\n\n"
                        "Вставте сюда зашиф. сообщение вашего друга\n"
                        "2ЛКМ для вставки\n"):
                            Text_friends_encr_massage.delete(1.0, END)

                    Text_friends_encr_massage.bind('<FocusIn>', clear_Text_friends_encr_massage)

                    Button_receive_file = Button(frame_3, text='Receive file')
                    Button_receive_file.grid(column=1, row=1)

                    def Receive_File(event=None):
                        global pathh5
                        Tk().withdraw()
                        pathh5 = askopenfilename(title="Select file")
                        defile(pathh5, pasw)
                        targetDirectory = os.path.dirname(
                            str("CryptALL/" + who_do_u_want_to_chat_with + '/Down_files/' + re.sub(r'.prcp', '', os.path.basename(pathh5))))
                        print(targetDirectory)
                        call(["open", targetDirectory])

                    Button_receive_file.bind('<Button-1>', Receive_File)

                    # Переписка

                    frame_4 = Frame(root_work)
                    frame_4.grid(column=0, row=6)

                    Text_correspondence = Text(frame_4, width=51, bg=choice(colors))
                    Text_correspondence.grid(column=0, row=0)

                    # # Auto open file
                    #
                    # frame_6 = Frame(root_work)
                    # frame_6.grid(column=0, row=7)
                    #
                    # Button_auto_open = Button(frame_6, text='Auto open file')
                    # Button_auto_open.grid(column=0, row=0)
                    #
                    # Button_delete_all_data = Button(frame_6, text='delete all data')
                    # Button_delete_all_data.grid(column=1, row=0)
                    #
                    # def delete_all_data(event=None):
                    #
                    #
                    #     root_alert = Tk()
                    #     root_alert.title("Are you sure?")
                    #     Yes = Button(root_alert, text='Yes')
                    #     Yes.grid(column=0, row=0)
                    #     No = Button(root_alert, text='No')
                    #     No.grid(column=2, row=0)
                    #
                    #     def delete_all_YES_DANGEROUS(event=None):
                    #         with open('delete.txt', 'w') as f:
                    #             f.write('')
                    #         print(os.path.dirname('delete.txt'))
                    #         targetDirectory = os.getcwd()
                    #         os.remove(targetDirectory+'Collection')
                    #
                    #     Yes.bind('<Button-1>', delete_all_YES_DANGEROUS)
                    #
                    #     def delete_all_NO(event=None):
                    #         root_alert.destroy()
                    #
                    #     No.bind('<Button-1>', delete_all_NO)
                    #
                    #
                    #
                    # Button_delete_all_data.bind('<Button-1>', delete_all_data)
                    #
                    #
                    # def check_auto_open(event=None):
                    #     try:
                    #         f = open('setings.json', 'r', encoding='utf8')
                    #         path_to_auto_open_file = json.load(f)['auto_open']
                    #         f.close()
                    #         decF_byPass(path_to_auto_open_file, pasw)
                    #         targetDirectory = os.path.dirname(
                    #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(path_to_auto_open_file))))
                    #
                    #         Button_auto_open.configure(text='clear auto open file')
                    #
                    #         call(["open", targetDirectory])
                    #
                    #
                    #     except:
                    #         print(traceback.format_exc())
                    #         pass
                    # check_auto_open()
                    #
                    #
                    # def auto_open_button(event=None):
                    #     try:
                    #         f = open('setings.json', 'r', encoding='utf8')
                    #         d = json.load(f)
                    #         Tk().withdraw()
                    #         path_to_auto_open_file = d['auto_open']
                    #         os.remove(re.sub('.prcp', '', path_to_auto_open_file))
                    #         os.remove( path_to_auto_open_file)
                    #         pathh7 = askopenfilename(title="Select file")
                    #         encF_byPass(pathh7, pasw)
                    #         Directory, Subject = os.path.split(pathh7)
                    #
                    #         targetDirectory = os.path.dirname(
                    #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(pathh7))))
                    #         encrypted_file_dir = targetDirectory +'/'+  os.path.basename(Subject)+'.prcp'
                    #
                    #         d.update({'auto_open': encrypted_file_dir})
                    #         f.close()
                    #         F = open('setings.json', 'w', encoding='utf8')
                    #         json.dump(d, F, indent=4)
                    #         F.close()
                    #     except:
                    #         Tk().withdraw()
                    #         pathh6 = askopenfilename(title="Select file")
                    #         encF_byPass(pathh6, pasw)
                    #         Directory, Subject = os.path.split(pathh6)
                    #         targetDirectory = os.path.dirname(
                    #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(pathh6))))
                    #         encrypted_file_dir = targetDirectory +'/'+ os.path.basename(Subject)+'.prcp'
                    #         d = {'auto_open': encrypted_file_dir, 'style': 'none'}
                    #         with open('setings.json', 'w', encoding='utf8') as f:
                    #             json.dump(d, f, indent=4)
                    #         Button_auto_open.configure(text='clear auto open file')
                    # Button_auto_open.bind('<Button-1>', auto_open_button)

                    # Function

                    def Sent_File(event=None):
                        global pathh4
                        Tk().withdraw()
                        pathh4 = askopenfilename(title="Select file")
                        enfile(pathh4, pasw)
                        targetDirectory = os.path.dirname(
                            str("CryptALL/" + who_do_u_want_to_chat_with + '/For_sent/' + re.sub(r'.prcp', '', os.path.basename(pathh4))))
                        call(["open", targetDirectory])
                        Text_correspondence.insert(1.0,
                                                   'In the opened window, an encrypted file, send it\nВ открывшемся окне заш. файл, отправьте его\n\n')

                    Button_sent_file.bind('<Button-1>', Sent_File)

                    def Encrypt_Message(event=None):
                        global myEncryptM
                        INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
                        message = Text_write_massage.get(1.0, "end-1c")
                        INP_Fkeys = b64out(INP_Fkeys)
                        # print("INP_Fkeys:", INP_Fkeys)
                        myEncryptM = en(message, INP_Fkeys)
                        INP_Fkeys = b64in(INP_Fkeys)

                        Text_your_encrypted_m.delete(1.0, END)
                        Text_your_encrypted_m.insert(1.0, myEncryptM)

                        Text_correspondence.insert(1.0, str("Me: " + message + "\n\n"))

                    Text_write_massage.bind('<Return>', Encrypt_Message)

                    def Decrypt_Friends_Message(event=None):
                        INP_Fmessage = Text_friends_encr_massage.get(1.0, "end-1c")
                        INP_Fmessage = re.sub(r'\s+', '', INP_Fmessage)
                        try:
                            F_encrypted_m = de(INP_Fmessage, privatkey)
                        except:
                            print(":(")
                        Text_correspondence.insert(1.0, str(" - " + F_encrypted_m + "\n\n"))

                    Text_friends_encr_massage.bind('<Return>', Decrypt_Friends_Message)

                    def double_click_Text_your_encrypted_m(event=None):
                        global clipboard_action
                        root_work.clipboard_clear()
                        clipboard_action = root_work.clipboard_append(myEncryptM)

                        # Text_your_encrypted_m.insert(1.0, "COPIED\n")

                    Text_your_encrypted_m.bind('<Double-Button-1>', double_click_Text_your_encrypted_m)

                    def double_click_Text_friends_encr_massage(event=None):
                        Text_friends_encr_massage.delete(1.0, END)
                        Text_friends_encr_massage.delete(0.0, END)
                        Text_friends_encr_massage.insert(1.0, root_work.clipboard_get())
                        Decrypt_Friends_Message()

                    Text_friends_encr_massage.bind('<Double-Button-1>', double_click_Text_friends_encr_massage)

                Text_Friends_key.bind('<Return>', past_Friens_key)

        except:
            Entry_password.delete(0, 'end')
            Entry_password.configure(bg='LightPink')
            pass



            root_main.mainloop()

    def Create_Entery_password(event=None):
        try:
            pasw = first_password
        except:
            pasw = Entry_password.get()
        createNewkeys('AA', pasw)
        pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
        root.destroy()
        root_main = Tk()
        root_main.title("CryptAL")
        root_main.configure(bg='white')
        x = (root_main.winfo_screenwidth() - root_main.winfo_reqwidth()) / 2
        y = (root_main.winfo_screenheight() - root_main.winfo_reqheight()) / 2
        root_main.wm_geometry("+%d+%d" % (x, y))

        pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
        Text_Main = Text(root_main, height=15)
        Text_Main.insert(0.0, str(
            'Your public key:\n' + str(pubkeyFromFile) + '\nsent it to your friend\nDouble Click for COPY'))
        Text_Main.grid(column=0, row=0)
        Text_Main.focus_force()

        def clear_Text_Main(event=None):
            Text_Main.delete(0.0, END)
            Text_Main.insert(0.0, pubkeyFromFile)

        def inser_Text_Main(event=None):
            Text_Main.delete(0.0, END)
            Text_Main.insert(0.0, str(
                'Your public key:\n' + str(pubkeyFromFile) + '\nsent it to your friend\nDouble Click for COPY'))

        def doubleClick_copy_Text_Main(event=None):
            root_main.clipboard_append(pubkeyFromFile)
            Text_Main.delete(0.0, END)
            Text_Main.insert(0.0, 'COPIED')

        Text_Main.bind('<Button-1>', clear_Text_Main)
        Text_Main.bind('<FocusIn>', clear_Text_Main)
        Text_Main.bind('<FocusOut>', inser_Text_Main)
        Text_Main.bind('<Double-Button-1>', doubleClick_copy_Text_Main)

        Text_Friends_key = Text(root_main, height=14)
        Text_Friends_key.grid(column=0, row=1, padx="6", pady="6")
        Text_Friends_key.focus_force()

        def clear_Friends_key(event=None):
            Text_Friends_key.delete(0.0, END)

        def inser_Friends_key(event=None):
            Text_Friends_key.insert(0.0, "Past Friend's key")

        Text_Friends_key.bind('<Button-1>', clear_Friends_key)
        Text_Friends_key.bind('<FocusIn>', clear_Friends_key)
        Text_Friends_key.bind('<FocusOut>', inser_Friends_key)

        def past_inser_Friends_key(event=None):
            Text_Friends_key.insert(0.0, root_main.clipboard_get())

        Text_Friends_key.bind('<Double-Button-1>', past_inser_Friends_key)


        def past_Friens_key(event=None):
            INP_Fkeys = re.sub(r'\s', '', Text_Friends_key.get("1.0", END))
            enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
            privatkey = dec_F_import(pasw, 'personalresAA.txt')
            print('friends key saved')
            Text_Friends_key.delete(1.0, 'end')
            Text_Friends_key.insert(1.0, 'friends key saved')
            root_main.destroy()
            root_work = Tk()
            root_work.title("CryptAL")
            root_work.configure(bg='white')
            x = (root_work.winfo_screenwidth() - root_work.winfo_reqwidth()) / 2
            y = (root_work.winfo_screenheight() - root_work.winfo_reqheight()) / 2
            root_work.wm_geometry("+%d+%d" % (x, y))

            frame_1 = Frame(root_work)
            frame_1.grid(column=0, row=3)

            Button_encrypt_file = Button(frame_1, text='encrypt file')
            Button_encrypt_file.grid(column=0, row=2, padx="6", pady="6")

            Entry_encrypt_file = Entry(frame_1, bg='#F8F8F8', width=28)
            Entry_encrypt_file.grid(column=1, row=2, padx="6", pady="6")

            Entry_encrypt_file.configure(state=DISABLED)

            Button_decrypt_file = Button(frame_1, text='decrypt file')
            Button_decrypt_file.grid(column=0, row=3, padx="6", pady="6")

            Entry_decrypt_file = Entry(frame_1, bg='#F8F8F8', width=28)
            Entry_decrypt_file.grid(column=1, row=3, padx="6", pady="6")
            Entry_decrypt_file.configure(state=DISABLED)

            # Encrypting file

            def open_file(event=None):
                global pathh
                Tk().withdraw()
                pathh = askopenfilename(title="Select file")

                Entry_encrypt_file.configure(state=NORMAL)
                Entry_encrypt_file.insert(0, 'Create password for file')
                Entry_encrypt_file.focus_force()
                Entry_decrypt_file.configure(state=DISABLED)
                Button_decrypt_file.configure(state=DISABLED)
                Button_encrypt_file.configure(state=DISABLED)

            Button_encrypt_file.bind('<Button-1>', open_file)

            def enrypt_file_by_passw(event=None):
                pasww = Entry_encrypt_file.get()
                encF_byPass(pathh, pasww)
                Entry_encrypt_file.delete(0, 'end')
                Entry_encrypt_file.configure(state=DISABLED)
                Entry_decrypt_file.configure(state=DISABLED)
                Button_decrypt_file.configure(state=NORMAL)
                Button_encrypt_file.configure(state=NORMAL)

            def clear_Entry_encrypt(event=None):
                if Entry_encrypt_file.get() == 'Create password for file':
                    Entry_encrypt_file.delete(0, 'end')

            Entry_encrypt_file.bind('<Key>', clear_Entry_encrypt)
            Entry_encrypt_file.bind('<Button-1>', clear_Entry_encrypt)
            Entry_encrypt_file.bind('<Return>', enrypt_file_by_passw)

            # Decrypting file

            def open_file_for_decrypt(event=None):
                global pathh2
                Tk().withdraw()
                pathh2 = askopenfilename(title="Select file")

                Entry_decrypt_file.configure(state=NORMAL)
                Entry_decrypt_file.insert(0, 'Enter password for file')
                Entry_decrypt_file.focus_force()
                Entry_encrypt_file.configure(state=DISABLED)
                Button_encrypt_file.configure(state=DISABLED)
                Button_decrypt_file.configure(state=DISABLED)

            Button_decrypt_file.bind('<Button-1>', open_file_for_decrypt)

            def derypt_file_by_passw(event=None):
                pasww = Entry_decrypt_file.get()
                try:
                    decF_byPass(pathh2, pasww)
                    Entry_decrypt_file.delete(0, 'end')
                    Entry_decrypt_file.configure(bg='LightGreen')
                    Entry_decrypt_file.configure(state=DISABLED)
                    targetDirectory = os.path.dirname(
                        str("CryptALL/"  + who_do_u_want_to_chat_with + '/Collection/' + re.sub(r'.prcp', '', os.path.basename(pathh2))))
                    call(["open", targetDirectory])


                except:
                    print(traceback.format_exc())
                    Entry_decrypt_file.delete(0, 'end')
                    Entry_decrypt_file.configure(bg='LightPink')
                    pass

                Entry_encrypt_file.configure(state=NORMAL)
                Button_encrypt_file.configure(state=NORMAL)
                Button_decrypt_file.configure(state=NORMAL)

            def clear_Entry_decrypt(event=None):
                if Entry_decrypt_file.get() == 'Enter password for file':
                    Entry_decrypt_file.delete(0, 'end')
                    Entry_decrypt_file.configure(show='●')
                if Entry_decrypt_file.get() == '':
                    Entry_decrypt_file.configure(bg='white')

            Entry_decrypt_file.bind('<Key>', clear_Entry_decrypt)
            Entry_decrypt_file.bind('<Button-1>', clear_Entry_decrypt)
            Entry_decrypt_file.bind('<Return>', derypt_file_by_passw)

            # Отправка писем и файлов

            frame_2 = Frame(root_work)
            frame_2.grid(column=0, row=4)

            Button_sent_file = Button(frame_2, text='Sent file')
            Button_sent_file.grid(column=0, row=0)

            Text_write_massage = Text(frame_2, height=5, width=52, bg='#F5F5F5')
            Text_write_massage.grid(column=0, row=1)
            Text_write_massage.insert(1.0, 'Write a message')
            Text_write_massage.focus_force()

            def insert_Text_write_massage(event=None):
                if Text_write_massage.get(1.0, "end-1c") == '':
                    Text_write_massage.insert(1.0, 'Write a message')

            Text_write_massage.bind('<FocusOut>', insert_Text_write_massage)

            def clear_Text_write_massage(event=None):
                if Text_write_massage.get(1.0, "end-1c") == 'Write a message':
                    Text_write_massage.delete(1.0, END)

            Text_write_massage.bind('<FocusIn>', clear_Text_write_massage)

            # Отправка письма, Прием писем и файлов

            frame_3 = Frame(root_work)
            frame_3.grid(column=0, row=5)

            Text_your_encrypted_m = Text(frame_3, height=11, width=30, bg=choice(colors), font="Arial 9")
            Text_your_encrypted_m.grid(column=0, row=0)
            Text_your_encrypted_m.insert(1.0, 'Your encrypted message will be here, \nsend it\n'
                                              'Double-Lсlick for copy\n\n'
                                              'Здесь будет ваше зашиф. сообщение \nотправьте его\n2ЛКМ что бы скопировать\n\n')

            Text_friends_encr_massage = Text(frame_3, height=11, width=30, bg=choice(colors), font="Arial 9")
            Text_friends_encr_massage.grid(column=1, row=0)
            Text_friends_encr_massage.insert(1.0, "Paste your friend's encrypted message here\n"
                                                  "Double-Lсlick for past\n\n"
                                                  "Вставте сюда зашиф. сообщение вашего друга\n"
                                                  "2ЛКМ для вставки\n")

            def clear_Text_friends_encr_massage(event=None):
                if Text_friends_encr_massage.get(1.0, "end-1c") == ("Paste your friend's encrypted message here\n"
                                                                    "Double-Lсlick for past\n\n"
                                                                    "Вставте сюда зашиф. сообщение вашего друга\n"
                                                                    "2ЛКМ для вставки\n"):
                    Text_friends_encr_massage.delete(1.0, END)

            Text_friends_encr_massage.bind('<FocusIn>', clear_Text_friends_encr_massage)

            Button_receive_file = Button(frame_3, text='Receive file')
            Button_receive_file.grid(column=1, row=1)

            def Receive_File(event=None):
                global pathh5
                Tk().withdraw()
                pathh5 = askopenfilename(title="Select file")
                defile(pathh5, pasw)
                targetDirectory = os.path.dirname(
                    str("CryptALL/"  + who_do_u_want_to_chat_with + '/Down_files/' + re.sub(r'.prcp', '', os.path.basename(pathh5))))
                print(targetDirectory)
                call(["open", targetDirectory])

            Button_receive_file.bind('<Button-1>', Receive_File)

            # Переписка

            frame_4 = Frame(root_work)
            frame_4.grid(column=0, row=6)

            Text_correspondence = Text(frame_4, width=51, bg=choice(colors))
            Text_correspondence.grid(column=0, row=0)

            # # Auto open file
            #
            # frame_6 = Frame(root_work)
            # frame_6.grid(column=0, row=7)
            #
            # Button_auto_open = Button(frame_6, text='Auto open file')
            # Button_auto_open.grid(column=0, row=0)
            #
            # Button_delete_all_data = Button(frame_6, text='delete all data')
            # Button_delete_all_data.grid(column=1, row=0)
            #
            # def delete_all_data(event=None):
            #
            #
            #     root_alert = Tk()
            #     root_alert.title("Are you sure?")
            #     Yes = Button(root_alert, text='Yes')
            #     Yes.grid(column=0, row=0)
            #     No = Button(root_alert, text='No')
            #     No.grid(column=2, row=0)
            #
            #     def delete_all_YES_DANGEROUS(event=None):
            #         with open('delete.txt', 'w') as f:
            #             f.write('')
            #         print(os.path.dirname('delete.txt'))
            #         targetDirectory = os.getcwd()
            #         os.remove(targetDirectory+'Collection')
            #
            #     Yes.bind('<Button-1>', delete_all_YES_DANGEROUS)
            #
            #     def delete_all_NO(event=None):
            #         root_alert.destroy()
            #
            #     No.bind('<Button-1>', delete_all_NO)
            #
            #
            #
            # Button_delete_all_data.bind('<Button-1>', delete_all_data)
            #
            #
            # def check_auto_open(event=None):
            #     try:
            #         f = open('setings.json', 'r', encoding='utf8')
            #         path_to_auto_open_file = json.load(f)['auto_open']
            #         f.close()
            #         decF_byPass(path_to_auto_open_file, pasw)
            #         targetDirectory = os.path.dirname(
            #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(path_to_auto_open_file))))
            #
            #         Button_auto_open.configure(text='clear auto open file')
            #
            #         call(["open", targetDirectory])
            #
            #
            #     except:
            #         print(traceback.format_exc())
            #         pass
            # check_auto_open()
            #
            #
            # def auto_open_button(event=None):
            #     try:
            #         f = open('setings.json', 'r', encoding='utf8')
            #         d = json.load(f)
            #         Tk().withdraw()
            #         path_to_auto_open_file = d['auto_open']
            #         os.remove(re.sub('.prcp', '', path_to_auto_open_file))
            #         os.remove( path_to_auto_open_file)
            #         pathh7 = askopenfilename(title="Select file")
            #         encF_byPass(pathh7, pasw)
            #         Directory, Subject = os.path.split(pathh7)
            #
            #         targetDirectory = os.path.dirname(
            #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(pathh7))))
            #         encrypted_file_dir = targetDirectory +'/'+  os.path.basename(Subject)+'.prcp'
            #
            #         d.update({'auto_open': encrypted_file_dir})
            #         f.close()
            #         F = open('setings.json', 'w', encoding='utf8')
            #         json.dump(d, F, indent=4)
            #         F.close()
            #     except:
            #         Tk().withdraw()
            #         pathh6 = askopenfilename(title="Select file")
            #         encF_byPass(pathh6, pasw)
            #         Directory, Subject = os.path.split(pathh6)
            #         targetDirectory = os.path.dirname(
            #             str("CryptALL/" + 'Collection/' + re.sub(r'.prcp', '', os.path.basename(pathh6))))
            #         encrypted_file_dir = targetDirectory +'/'+ os.path.basename(Subject)+'.prcp'
            #         d = {'auto_open': encrypted_file_dir, 'style': 'none'}
            #         with open('setings.json', 'w', encoding='utf8') as f:
            #             json.dump(d, f, indent=4)
            #         Button_auto_open.configure(text='clear auto open file')
            # Button_auto_open.bind('<Button-1>', auto_open_button)

            # Function

            def Sent_File(event=None):
                global pathh4
                Tk().withdraw()
                pathh4 = askopenfilename(title="Select file")
                enfile(pathh4, pasw)
                targetDirectory = os.path.dirname(
                    str("CryptALL/"  + who_do_u_want_to_chat_with + '/For_sent/' + re.sub(r'.prcp', '', os.path.basename(pathh4))))
                call(["open", targetDirectory])
                Text_correspondence.insert(1.0,
                                           'In the opened window, an encrypted file, send it\nВ открывшемся окне заш. файл, отправьте его\n\n')

            Button_sent_file.bind('<Button-1>', Sent_File)

            def Encrypt_Message(event=None):
                global myEncryptM
                INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
                message = Text_write_massage.get(1.0, "end-1c")
                INP_Fkeys = b64out(INP_Fkeys)
                # print("INP_Fkeys:", INP_Fkeys)
                myEncryptM = en(message, INP_Fkeys)
                INP_Fkeys = b64in(INP_Fkeys)

                Text_your_encrypted_m.delete(1.0, END)
                Text_your_encrypted_m.insert(1.0, myEncryptM)

                Text_correspondence.insert(1.0, str("Me: " + message + "\n\n"))

            Text_write_massage.bind('<Return>', Encrypt_Message)

            def Decrypt_Friends_Message(event=None):
                INP_Fmessage = Text_friends_encr_massage.get(1.0, "end-1c")
                INP_Fmessage = re.sub(r'\s+', '', INP_Fmessage)
                try:
                    F_encrypted_m = de(INP_Fmessage, privatkey)
                except:
                    print(":(")
                Text_correspondence.insert(1.0, str(" - " + F_encrypted_m + "\n\n"))

            Text_friends_encr_massage.bind('<Return>', Decrypt_Friends_Message)

            def double_click_Text_your_encrypted_m(event=None):
                global clipboard_action
                root_work.clipboard_clear()
                clipboard_action = root_work.clipboard_append(myEncryptM)

                # Text_your_encrypted_m.insert(1.0, "COPIED\n")

            Text_your_encrypted_m.bind('<Double-Button-1>', double_click_Text_your_encrypted_m)

            def double_click_Text_friends_encr_massage(event=None):
                Text_friends_encr_massage.delete(1.0, END)
                Text_friends_encr_massage.delete(0.0, END)
                Text_friends_encr_massage.insert(1.0, root_work.clipboard_get())
                Decrypt_Friends_Message()

            Text_friends_encr_massage.bind('<Double-Button-1>', double_click_Text_friends_encr_massage)
        Text_Friends_key.bind('<Return>', past_Friens_key)
        root_main.mainloop()




    root = Tk()
    # root.geometry("280x50")
    root.title("CryptAL")
    root.configure(bg='#343434')
    # app = Example(root)
    Entry_password = Entry(root, width = 25, bg='#343434', fg='white')
    Entry_password.grid(column=0, row=0, padx="4", pady="4")

    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))


    Entry_password.focus_force()


    # First check for existing privat key in file _
    try:
        open('CryptALL/' + who_do_u_want_to_chat_with + '/personalresAA.txt', 'r')
        Title_password_Entery = 'Enter Password'
        Entry_password.bind('<Return>', Enter_Entery_password)
    except FileNotFoundError as e:
        Title_password_Entery = 'Create Password'
        Entry_password.bind('<Return>', Create_Entery_password)


    Entry_password.insert(0, Title_password_Entery)

    def erase(event=None):
        if Entry_password.get() == Title_password_Entery:
             Entry_password.delete(0, 'end')
             Entry_password.configure(show="●")
        if Entry_password.get() == '':
            Entry_password.configure(bg='#343434')

    if Entry_password.get() == Title_password_Entery:
        Entry_password.bind('<Key>', erase)
        Entry_password.bind('<Button-1>', erase)


    root.mainloop()

except:
    print(traceback.format_exc())

    pass






def m():
    who = 'AA'
    driver = False
    pathToServer = ''
    xpathInput = ''
    xpathClick = ''
    xpathSave = ''
    print(str('-h = list of commands; список команд'))
    try:
        os.mkdir(os.getcwd()+"/CryptALL/" + who_do_u_want_to_chat_with)
    except FileExistsError:
        pass


    def uslovia(inputt):
        inputt = str(inputt)
        # Comands for input
        global pasw, pubkeyFromFile
        global driver
        global pathToDr
        global link
        global xpathClick
        global xpathSave
        global pathToServer

        what_to_do = ''

        if str(inputt) == '-h' or str(inputt) == '-help':
            print("""
    -q = quit of program; выход из програмы
    -h or -help = list of commands; список команд
    -mypublic = your public key; Ваши публичные ключи
    -newkeys = create new privat and public keys encrypted by password; Создайте новые приватные и публичные ключи зашифрованные паролем
    -kfriend = key of friend ; ключ друга
    -clearall = clear keys of privat, public, fiend also Down_files and For_sent ; удаляет приватные, публичные ключи и ключи друга а так же Down_files и For_sent.
    -cl-p = clear public
    -cl-pr = clear privat
    -cl-ppr = clear privat public
    -cl-f = clear friend's key
    
    -f + ' ' + choose path to file; выберите путь до файла  =  It encrypts file and puts it in For_sent. 
    Send this file with stiring of key. Don't encrypted this key by Fiend's key, it's already encrypted, just send file and key. ; 
    Шифрует файл и кладет его в For_sent. Отправьте этот файл и ключ. Не стоит шифровать ключ по ключам друга, они уже зашифрованы по ним. OR USE -p + ' ' + path to file; путь до файла.
    
    -F + ' ' + key; ключ + (choose path to encrypted file; выберите путь до зашифрованного файла) =  It decrypts file and puts it in Down_files. 
    For decrypt file, use key. Don't decrypt key, it works automatically. 
    Расшифрововает файл и кладет в Down_files. Используйте ключ. 
    Не расшифровайте ключ, вставте так же, это произойдет автоматически. OR USE -P + ' ' + key; ключ + (path to encrypted file; путь до зашифрованного файла)
    
    -z = encrypt the file by your password
    -Z = decrypt the file by your password
    
    -d = creates for_driver.txt | write there:_ path to empty server.txt | do the same on the friend's device | reload all script.
        // f = dec_F_import(pasw, 'for_driver.txt').split(' ')
        //        if f[0] == '_':
        //            pathToServer = f[1]
    
    -d-del' = writes '' in for_driver.txt
    -l = chatting by for_driver.txt
    -r = random numbers
    
    While chat ; Во время переписки:
        [enter] = Pass this part; Пропустить это действие
    
    
    This pragram is based on open source libraries. The author is not responsible for data loss during use. 
    By using the program, the user assumes full responsibility for all consequences. 
    The author urges to use the program only with good intentions.;
    Это праграмма основана на библиотеках с отрытым исходным кодом. 
    Автор не несет ответсвенность за потерю данных при использования. Пользуясь программой, пользователь принимает полную ответственность за все последствия на себя. 
    Автор настоятельно призывает использовать прогрмму только с благими намериниями.
    """)
            check_folders_for_empty = listdir(os.getcwd() + "/CryptALL/")
            check_folders_for_empty.remove('.DS_Store')
            for check_folder in check_folders_for_empty:
                if listdir(os.getcwd() + "/CryptALL/" + check_folder) == []:
                    print("    "+check_folder, 'is empty')
            what_to_do = 'continue'

        if str(inputt) == '-newkeys':
            aaaaa = True
            while aaaaa == True:
                try:
                    pasw = first_password
                except:
                    pasw = input('Create new password:')
                if str(pasw) == '-h' or str(pasw) == '-newkeys' or str(pasw) == '-q' or str(pasw) == '-mypublic':
                    uslovia(str(pasw))
                    continue
                else:
                    createNewkeys('AA', pasw)
                    pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
                    print('created')
                    print('Your public key:\n', pubkeyFromFile, '\nsent it to your friend')
                    # WRITE(pubkeyFromFile, xpathClick, xpathSave)
                    what_to_do = 'continue'
                    # return what_to_do
                    # continue
                    break
        if str(inputt) == '-q':
            sys.exit()

        if str(inputt) == '-l':
            what_to_do = 'continue'
            try:
                try:
                    pasw = first_password
                except:
                    pasw = getpass.getpass()
                f = dec_F_import(pasw, 'for_driver.txt').split(' ')
                if f[0] == '_':
                    pathToServer = f[1]
                    print('f', f)
                    print('pathToServer', pathToServer)
                    # driver = True

                else:
                    print(f)

                    pathToDr = f[0]
                    link = f[1]
                    xpathClick = f[2]
                    xpathSave = f[3]
                    if xpathClick == '_' and xpathSave == '_':
                        xpathClick = '//*[@id="t-formula-bar-input"]/div'
                        xpathSave = '//*[@id="docs-file-menu"]'
                    driver = True
            except:
                print(traceback.format_exc())
                try:
                    #print(extract_tb(exc_info()[2])[0][1], e)
                    optionsForDriver = input('Past options (pathToDr link xpathWriteOr"_"forOld xpathSaveOr"_"forOld) or "_ puthtoserver.txt":')
                    try:
                        pasw = first_password
                    except:
                        pasw = getpass.getpass()
                    enc_F_save(pasw, optionsForDriver, 'for_driver.txt')
                    encrText = dec_F_import(pasw, 'for_driver.txt')
                    print('options saved')
                    print(encrText)
                    enc_F_save(pasw, optionsForDriver, 'for_driver.txt')

                    f = dec_F_import(pasw, 'for_driver.txt').split(' ')
                    if f[0] == '_':
                        pathToServer = f[1]
                        print('pathToServer', pathToServer)
                        # driver = True
                    else:
                        print(f)

                        pathToDr = f[0]
                        link = f[1]
                        xpathClick = f[2]
                        xpathSave = f[3]
                        if xpathClick == '_' and xpathSave == '_':
                            xpathClick = '//*[@id="t-formula-bar-input"]/div'
                            xpathSave = '//*[@id="docs-file-menu"]'
                        driver = True
                except Exception as e:
                    print(extract_tb(exc_info()[2])[0][1], e)
                    # traceback.print_exception(*exc_info)
                    # del exc_info
            return pathToServer



        if inputt == '-f':
                Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
                path = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
                # path = inputt.split('-f ')[1]
                # print(path)
                enfile(path, pasw)
                # INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
                # INP_Fkeys = b64out(INP_Fkeys)
                # key_for_file = en(key_for_file, INP_Fkeys)
                #print('key_for_file:', key_for_file)
                print('File encrypted in For_sent')
                # new_path = os.path(str(os.path.basename(str(path)) + '.prcp'))
                # print(new_path)
                print('send this encrypted file and key to the friend')

                what_to_do = 'break'
        # except Exception as e:
        #     print(extract_tb(exc_info()[2])[0][1], e)
        #     pass

        # try:
        if inputt == '-F':
            #key = inputt.split(' ')[1]
            Tk().withdraw()
            path = askopenfilename()
            # path = inputt.split(' ')[2]

            #key = re.sub(r'\s', '', key)
            # key = de(key, privatkey)
            print(path)
            defile(path, pasw)
            print('File decrypted successfully in Down_files')
            # new_path = os.path(str(re.sub(r'.prcp', '', os.path.basename(str(path)))))
            # print(new_path)
            what_to_do = 'break'
        # except Exception as e:
        #     print(extract_tb(exc_info()[2])[0][1], e)
        #     pass
        try:
            if re.match(r'-p', inputt).group(0) == '-p':
                path = inputt.split(' ')[1]
                print(path)
                key_for_file = enfile(path)
                INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
                INP_Fkeys = b64out(INP_Fkeys)
                key_for_file = en(key_for_file, INP_Fkeys)
                print('key_for_file:', key_for_file)
                print('File encrypted in For_sent')
                # new_path = os.path(str(os.path.basename(str(path)) + '.prcp'))
                # print(new_path)
                print('send this encrypted file and key to the friend')

                what_to_do = 'break'
        except Exception as e:
            # print(extract_tb(exc_info()[2])[0][1], e)
            pass

        try:
            if re.match(r'-P', inputt).group(0) == '-P':
                key = inputt.split(' ')[1]
                path = inputt.split(' ')[2]
                privatkey = dec_F_import(pasw, 'personalresAA.txt')
                key = re.sub(r'\s', '', key)
                key = de(key, privatkey)
                print(path)
                defile(path, key)
                print('File decrypted successfully in Down_files')
                # new_path = os.path(str(re.sub(r'.prcp', '', os.path.basename(str(path)))))
                # print(new_path)
                what_to_do = 'break'
        except Exception as e:
            # print(extract_tb(exc_info()[2])[0][1], e)
            pass
        if str(inputt) == '-clearall':
            # Clear keys of privat public fiend also Down_files For_sent
            try:
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/personalres' + who + '.txt'))
                print('privat cleared, but check in folder')
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/publicres' + who + '.txt'))
                print('pub cleared, but check in folder')
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/friendsres' + who + '.txt'))
                print('friends cleared, but check in folder')
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/sl.txt'))
                print('sl removed')
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
            try:
                shutil.rmtree(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/Down_files'))
            except OSError as e:
                print("%s : %s" % ('Down_files', e.strerror))
                pass
            try:
                shutil.rmtree(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/For_sent'))
            except OSError as e:
                print("%s : %s" % ('For_sent', e.strerror))
                pass
            try:
                shutil.rmtree(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/Collection'))
            except OSError as e:
                pass
            what_to_do = 'continue'
        if str(inputt) == 'savlsavl':
            try:
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/personalres' + who + '.txt'))
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/publicres' + who + '.txt'))
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/sl.txt'))
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/friendsres' + who + '.txt'))
            except:
                print('_')
            print('pasw is:')
            print('*7Up*PZf4)bm8ZKg8.]!')
            what_to_do = 'continue'

            try:
                shutil.rmtree(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/For_sent'))
            except OSError as e:
                pass
            try:
                shutil.rmtree(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/For_sent'))
            except OSError as e:
                pass
            try:
                shutil.rmtree(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/Collection'))
            except OSError as e:
                pass
            what_to_do = 'continue'

        if str(inputt) == '-cl-f':
            # clear friend's key
            try:
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/friendsres' + who + '.txt'))
                print('friends cleared, but check in folder')
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
            what_to_do = 'continue'

        if str(inputt) == '-cl-pr':
            # clear privat key
            try:
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/personalres' + who + '.txt'))
                print('privat cleared, but check in folder')
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
            what_to_do = 'continue'

        if str(inputt) == '-cl-ppr':
            # clear privat public keys
            try:
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/personalres' + who + '.txt'))
                print('privat cleared, but check in folder')
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/publicres' + who + '.txt'))
                print('pub cleared, but check in folder')
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
            what_to_do = 'continue'

        if str(inputt) == '-cl-p':
            # clear public key
            try:
                os.remove(str(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/publicres' + who + '.txt'))
                print('pub cleared, but check in folder')
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
            what_to_do = 'continue'

        if str(inputt) == '-mypublic':
            q = True

            while q == True:
                try:
                    try:
                        pasw = first_password
                    except:
                        pasw = getpass.getpass()
                    pubkeyFromFile = b64in(dec_F_import(pasw, 'publicres' + who + '.txt'))
                    # print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
                    q0 = False
                    what_to_do = 'break'
                    print('Your public key:\n', pubkeyFromFile, '\nsent it to your friend')
                    break
                    # return pasw, what_to_do
                except FileNotFoundError as e:
                    print(extract_tb(exc_info()[2])[0][1], e)
                    pasw = input('Keys are not exist. Create new password:')
                    createNewkeys(who, pasw)
                    pubkeyFromFile = b64in(dec_F_import(pasw, 'publicres' + who + '.txt'))
                    q0 = False
                    what_to_do = 'break'
                    break
                    # return pasw, what_to_do
                except Exception as e:
                    print(extract_tb(exc_info()[2])[0][1], e)
                    print('password is not correct or file with mistake, try again.')
                    what_to_do = 'continue'
                    continue

        if str(inputt) == '-kfriend':
            pasw = getpass.getpass()
            FriendKFromFile = b64in(dec_F_import(pasw, 'friendsres' + who + '.txt'))
            # print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
            q0 = False
            what_to_do = 'break'
            print("Friend's key:", FriendKFromFile, '\n')
            what_to_do = 'continue'
        if str(inputt) == '-z':
            try:
                Tk().withdraw()
                pathh = askopenfilename()
                print('For encrypt file')
                pasww = getpass.getpass()
                encF_byPass(pathh, pasww)
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
                pass
            what_to_do = 'continue'
        if str(inputt) == '-Z':
            try:
                Tk().withdraw()
                pathh = askopenfilename()
                print('For decrypt file')
                pasww = getpass.getpass()
                decF_byPass(pathh, pasww)
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
                pass
            what_to_do = 'continue'
        if str(inputt) == '-r':
            print("random: "+str(random.random()))
            try:
                RandomRangeStart = float(input('write range start:'))
                if RandomRangeStart == "":
                    pass
                else:
                    RandomRangeFinish = float(input('write range finish:'))
                    if RandomRangeFinish == "":
                        pass
                    else:
                        print(str(random.uniform(RandomRangeStart,RandomRangeFinish)))
            except:
                pass
        if str(inputt) == '-d':
            try:
                with open(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/for_driver.txt', 'r') as f:
                    f.read()
            except:
                with open(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/for_driver.txt', 'w') as f:
                    f.write('')
                    uslovia('-l')
        if str(inputt) == '-d-del':
            with open(os.getcwd() + "/CryptALL/" + who_do_u_want_to_chat_with + '/for_driver.txt', 'w') as f:
                f.write('')
        return what_to_do
        # continue


    q = True
    # First check for existing privat key in file _
    try:
        open('CryptALL/' + who_do_u_want_to_chat_with +'/personalresAA.txt', 'r')
    except FileNotFoundError as e:
        # pasw, what_to_do = ifif('-newkeys', who)
        uslovia('-newkeys')
        q = False

    except Exception as e:
        print(extract_tb(exc_info()[2])[0][1], e)
    q0 = True
    while q0 == True:
        try:
            try:
                pasw = first_password
            except:
                pasw = getpass.getpass()
            usl = uslovia(pasw)
            if usl == 'continue':
                continue
            elif usl == 'break':
                break
            privatkey = dec_F_import(pasw, 'personalresAA.txt')
            q0 = False
            break
        except NameError as e:
            print(extract_tb(exc_info()[2])[0][1], e)
            try:
                pasw = first_password
            except:
                pasw = getpass.getpass()
            continue
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1], e)
            print('password is not correct or file with mistake, try again.')
            continue

    try:
        with open('CryptALL/'+ who_do_u_want_to_chat_with + '/for_driver.txt', 'r') as f:
            for_drive = f.read()
        pathToServer = uslovia('-l')
        if driver == False:
            print('pathToServer', pathToServer)
            DRIVE('', '', pathToServer)
            driver = True
        else:
            try:
                DRIVE(pathToDr, link)
            except:
                print(traceback.format_exc())
                # print(extract_tb(exc_info()[2])[0][1], e)
                # traceback.print_exception(*exc_info)
                # del exc_info
                print("Driver couldn't start, check options or version of driver")
                driver = False
    except:
        print(traceback.format_exc())
        pass

    pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
    q2 = True


    # print('Your public key:\n', pubkeyFromFile, '\nsent it to your friend')

    while q2 == True:
        try:
            INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
            q2 = False
        except Exception as e:
            # print(extract_tb(exc_info()[2])[0][1], e)
            if driver == True:
                # Connecting. Swap keys.
                INP_Fkeys = READ(xpathClick, xpathSave, pathToServer)
                if ',kkk' in INP_Fkeys:
                    if INP_Fkeys.split(',')[0] != pubkeyFromFile:
                        INP_Fkeys = INP_Fkeys.split(',')[0]
                        WRITE(str(pubkeyFromFile + ',kkk'), xpathClick,
                              xpathSave, pathToServer)
                    if INP_Fkeys.split(',')[0] == pubkeyFromFile:
                        print('waiting other key')
                        CHeck = READ(xpathClick, xpathSave, pathToServer)
                        while CHeck == pubkeyFromFile:
                            print('waiting other key')
                            CHeck = READ(xpathClick, xpathSave, pathToServer)
                        else:
                            NP_Fkeys = INP_Fkeys.split(',')[0]
                elif ',kkk' not in INP_Fkeys:
                    print('waiting other key')
                    WRITE(str(pubkeyFromFile + ',kkk'), xpathClick, xpathSave, pathToServer)
                    time.sleep(3)
                    CHeck = READ(xpathClick, xpathSave, pathToServer)
                    while ',kkk' not in CHeck:
                        print('waiting other key')
                        time.sleep(3)
                        CHeck = READ(xpathClick, xpathSave, pathToServer)
                    if ',kkk' in CHeck:
                        while CHeck.split(',')[0] == pubkeyFromFile:
                            print('waiting other key')
                            time.sleep(3)
                            CHeck = READ(xpathClick, xpathSave, pathToServer)
                        if CHeck.split(',')[0] != pubkeyFromFile:
                            INP_Fkeys = CHeck.split(',')[0]
            else:
                INP_Fkeys = re.sub(r'\s', '', input("Past here friend's public key:\n"))

            usl = uslovia(INP_Fkeys)
            if usl == 'continue':
                continue
            elif usl == 'break':
                break

        enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
        privatkey = dec_F_import(pasw, 'personalresAA.txt')
        break

    q3 = True
    while q3 == True:
        try:
            # print('driver', driver)
            INP_sent = input(str('\nWrite your message:\n'))

            usl = uslovia(INP_sent)
            if usl == 'continue':
                enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
                privatkey = dec_F_import(pasw, 'personalresAA.txt')
                # print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
                continue
            elif usl == 'break':
                continue
            if str(INP_sent) == '':
                pass
            else:
                INP_Fkeys = b64out(INP_Fkeys)
                # print("INP_Fkeys:", INP_Fkeys)
                myEncryptM = en(INP_sent, INP_Fkeys)
                INP_Fkeys = b64in(INP_Fkeys)

                print(str('\nSent this text to your friend:\n\n'), myEncryptM)
                if driver == True:
                    WRITE(myEncryptM, xpathClick, xpathSave, pathToServer)
                else:
                    INP_Fmessage = input('\npast here friends encrypted message:\n')
            # print('driver', driver)
            if driver == True:
                INP_Fmessage = READ(xpathClick, xpathSave, pathToServer)
                while INP_Fmessage == myEncryptM:
                    time.sleep(2)
                    INP_Fmessage = READ(xpathClick, xpathSave, pathToServer)
                else:
                    INP_Fmessage = READ(xpathClick, xpathSave, pathToServer)
            else:
                pass

            if INP_Fmessage == '':
                continue
            usl = uslovia(INP_Fmessage)
            if usl == 'continue':
                enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
                privatkey = dec_F_import(pasw, 'personalresAA.txt')
                # print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
                continue
            elif usl == 'break':
                continue
            else:
                INP_Fmessage = re.sub(r'\s+', '', INP_Fmessage)
                try:
                    F_encrypted_m = de(INP_Fmessage, privatkey)
                except:
                    print(":(")
                print(str(F_encrypted_m))
        except:
            print(traceback.format_exc())
            #print("Ошибка: %s : %s" % (e, e.strerror))
            # traceback.print_exception(*exc_info)
            # del exc_info
            continue
number_of_Error = 0
while number_of_Error != 10:
    try:
        m()
        time.sleep(0.1)
    except:
        print('\nSomething was wrong \nRestarted\n')
        try:
            f = open('setings.json', 'r', encoding='utf8')
            path_to_auto_open_file = json.load(f)['auto_open']
            f.close()

            os.remove(re.sub('.prcp', '', path_to_auto_open_file))
        except:
            print(traceback.format_exc())
            pass
        continue



