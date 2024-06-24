import tkinter as tk  # tkinter를 tk로 import
from tkinter import messagebox  # tkinter의 messagebox  import
from PIL import Image, ImageTk  # 이미지 처리를 위해 Pillow 라이브러리



class PhotoQuizApp:
    def __init__(self, root):
        self.root = root  # 전달받은 root를 인스턴스 변수로 저장
        self.root.title("과자 맞추기 퀴즈")  # 창 제목 설정
        self.root.geometry("1200x800")  # 창 크기 설정
        #self.root.configure(bg="#0033CC") # 창 배경색 설정



        self.background_image = Image.open("background_image.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo , text='test')
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1) #배경 전체에 사진
        


        self.title_label = tk.Label(root, text="과자 이름 맞추기",  # 제목라벨 생성
                                    font=("맑은 고딕", 24, "bold"), bg="#0033CC", fg="white") #라벨 폰트, 크기, 굵게, 텍스트 배경색, 텍스트 글자색
        self.title_label.pack(pady=20)  # 라벨 화면에 배치,위 아래 간격 조절

        self.image_label = tk.Label(root)  # 사진 보여줄 라벨 생성
        self.image_label.pack()  # 라벨화면에 띄우기

        self.answer_entry = tk.Entry(root, width=40)  # 답을 입력할 엔트리 생성
        self.answer_entry.pack(pady=10, ipadx=50, ipady=10)  # 엔트리 화면에 띄우고 크기설정(간격,가로 세로 너비)

        submit_image = Image.open("submit_image.png")  # 제출 버튼 이미지 열기
        submit_image = submit_image.resize((100, 50), Image.LANCZOS)  # 이미지 크기 조정
        submit_photo = ImageTk.PhotoImage(submit_image)  # 이미지를 tkinter용 PhotoImage로 변환
        self.submit_button = tk.Button(root, image=submit_photo, command=self.check_answer)  # 제출 버튼 생성
        self.submit_button.image = submit_photo  # 버튼의 이미지 설정
        self.submit_button.pack(pady=5)  # 버튼을 화면에 배치하고 간격을 주어 표시

        next_image = Image.open("next_image.png")  # 다음 사진으로 넘어가는 버튼 이미지 열기
        next_image = next_image.resize((70, 30), Image.LANCZOS)  # 이미지 크기 조정
        next_photo = ImageTk.PhotoImage(next_image)  # 이미지를 tkinter용 PhotoImage로 변환
        self.next_button = tk.Button(root, image=next_photo, command=self.show_next_photo)  # 다음 사진 버튼 생성
        self.next_button.image = next_photo  # 버튼의 이미지 설정
        self.next_button.pack(pady=5)  # 버튼을 화면에 배치하고 간격을 주어 표시

        self.photos = [("image1.png", "스윙칩"), ("image2.png", "포카칩"),  # 사진 ,정답 리스트
                       ("image3.png", "프링글스"), ("image4.png", "꼬깔콘"),
                       ("image5.png", "홈런볼")]
        self.current_photo = 0  # 현재 표시할 사진 인덱스 초기화

        self.show_photo()  # 첫 번째 사진 표시 

    def show_photo(self):
        photo_path, _ = self.photos[self.current_photo]  # 현재 사진의 파일 경로와 정답을 가져옴
        image = Image.open(photo_path)  # 이미지 파일 열기
        photo = ImageTk.PhotoImage(image)  # 이미지를 tkinter용으로 변환

        self.image_label.config(image=photo)  # 이미지 라벨에 이미지 설정
        self.image_label.image = photo  # 이미지 라벨의 이미지 설정

    def check_answer(self):
        _, correct_answer = self.photos[self.current_photo]  # 현재 사진의 정답 가져오기
        user_answer = self.answer_entry.get().strip().lower()  # 입력한 답 확인

        if user_answer == correct_answer.lower():  # 정답 확인
            messagebox.showinfo("결과", "정답!")  # 정답 메시지 표시
        else:
            messagebox.showinfo("결과", f"오답! 정답은: {correct_answer}")  # 오답 메시지 표시

    def show_next_photo(self):
        self.current_photo = (self.current_photo + 1) % len(self.photos)  # 다음 사진나오게
        self.show_photo()  # 다음 사진 표시 
        self.answer_entry.delete(0, tk.END)  # 답 입력 창 초기화

if __name__ == "__main__":
    root = tk.Tk()  # tkinter의 root 윈도우 생성
    app = PhotoQuizApp(root)  # PhotoQuizApp 클래스의 인스턴스 생성
    root.mainloop()  # 윈도우 이벤트 루프 시작
