from flask import Flask , render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Required,DataRequired,EqualTo


class RegisterForm(FlaskForm):
    # 用户名 不能为空
    name = StringField(label='用户名　', validators=[Required("用户名不能为空")])
    # 密码 不能为空
    password = PasswordField(label='密　码　', validators=[Required("密码不能为空")])
    # 确认密码  不能为空，并且与密码要一致
    repassword = PasswordField(label='确认密码', validators=[DataRequired("请输入确认密码！"),EqualTo('password', message="两次密码不一致！")])
    # 联系电脑 不能为空
    tel = StringField(label='联系电话', validators=[Required("联系电话不能为空")])
    submit = SubmitField(label="提交") # 提交按钮

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mrsoft'

@app.route('/register/', methods=['GET', 'POST'])  # 配置路由
def index():
    form = RegisterForm()
    data = {}
    if form.validate_on_submit():
        data['name'] = form.name.data
        data['password'] = form.password.data
        data['repassword'] = form.repassword.data
        data['tel'] = form.tel.data
    return render_template('register.html', form=form,data=data)

if __name__ == '__main__':
        app.run(debug=True)    
