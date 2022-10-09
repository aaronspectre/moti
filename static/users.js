let form = document.getElementById('add-form')
let form_cover = document.querySelector('#add-form .add-form-cover')



function userCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1

	form.querySelector('#name').value = card.querySelector('.user-first-name').innerText
	form.querySelector('#phone').value = card.querySelector('.user-phone-number').innerText
	form.querySelector('#role').value = card.querySelector('.user-role').innerText
	console.log(form.querySelector('#role').value)
}

form_cover.addEventListener('click', event => {
	form.style.display = 'none'
	form.style.opacity = 0
})