let form = document.getElementById('add-form')
let form_cover = document.querySelector('#add-form .add-form-cover')
let call_form_button = document.getElementById('call-form-button')

call_form_button.addEventListener('click', event => {
	form.style.display = 'flex';
	form.style.opacity = 1
	console.log('show')
})

form_cover.addEventListener('click', event => {
	form.style.display = 'none';
	form.style.opacity = 0
})