let form = document.getElementById('add-form')
let call_button = document.getElementById('call-form-button')
let form_cover = document.querySelector('#add-form .add-form-cover')


form_cover.addEventListener('click', event => {
	form.style.display = 'none'
	form.style.opacity = 0

	form.querySelectorAll('.add-form-user-roles small').forEach(item => item.remove())
})


call_button.addEventListener('click', event => {
	form.style.display = 'flex'
	form.style.opacity = 1

	form.querySelector('.add-category-form').setAttribute(
		'action',
		`${window.location.origin}${call_button.getAttribute('data-link')}`
	)

	form.querySelector('#price').value = ''
	form.querySelector('#payment').value = ''
	form.querySelector('#user-roles').value = ''
})


function appendRoles(roles){
	roles.forEach((role) => {
		item = document.createElement('small')
		item.appendChild(document.createTextNode(role))
		item.addEventListener('click', event => {
			event.target.remove()
			roles = form.querySelector('#user-roles').value.split(' | ')
			roles.splice(roles.indexOf(role.value), 1)
			form.querySelector('#user-roles').value = roles.join(' | ')
		})
		form.querySelector('.add-form-user-roles').appendChild(item)
	})
}


function userCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1

	form.querySelector('.add-category-form').setAttribute(
		'action',
		`${window.location.origin}/users/update/${card.querySelector('.user-id').innerText}`
	)

	form.querySelector('#name').value = card.querySelector('.user-first-name').innerText
	form.querySelector('#user-roles').value = card.querySelector('.user-role').innerText

	appendRoles(card.querySelector('.user-role').innerText.split(' | '))
}


function addRole(role){
	appendRoles([role.value])
	roles = form.querySelector('#user-roles').value.split(' | ')
	roles.push(role.value)
	form.querySelector('#user-roles').value = roles.join(' | ')
}


function feeCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1
	form.querySelector('.add-category-form').setAttribute(
		'action',
		`${window.location.origin}/fees/update/${card.querySelector('.fee-id').innerText}`
	)

	form.querySelector('#price').value = card.querySelector('.fee-price').innerText
	form.querySelector('#payment').value = card.querySelector('.fee-payment').innerText
}