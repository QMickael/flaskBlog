from wtforms import Form, StringField, TextAreaField, validators

class PostForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=60)])
    post_type = StringField('Category', [validators.Length(min=4, max=20)])
    content = TextAreaField('Content', [validators.DataRequired()])
