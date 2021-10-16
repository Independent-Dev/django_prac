from django import forms

class FileUploadForm(forms.Form):
    user_email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'mdl-textfield__input',
        'views.minlength':4,
        'maxlength':20,
        'autocomplete':'off', 
        'type':'email',
        'placeholder': 'user email'
    }))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'mdl-textfield__input'}))

    # 이건 나중에 구현해보기
    # def validate_file(self, field):
    #     _, ext = field.data.filename.split(".")
    #     if ext in current_app.config["POSSIBLE_FILE_EXTENSION"]:
    #         return True

    #     field.errors.append("txt 형식의 requirements 파일을 업로드해주세요!")
    #     return False