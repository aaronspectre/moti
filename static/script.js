let form = document.getElementById('add-form')
let panel_cover = document.getElementById('panel-cover')
let form_cover = document.querySelector('#add-form .add-form-cover')
let call_form_button = document.getElementById('call-form-button')
let products = Array()

call_form_button.addEventListener('click', event => {
	form.style.display = 'flex';
	form.style.opacity = 1

	form.querySelector('form').setAttribute('action', call_form_button.getAttribute('data-link'))

	input = form.querySelector('form')
	input.querySelector("[name = 'name_uz']").value = ''
	input.querySelector("[name = 'name_ru']").value = ''
	input.querySelector("[name = 'name_en']").value = ''

	input.querySelector("[name = 'image']").setAttribute('required', '')

	try{
		input.querySelector("[name = 'capacity']").value = ''
		input.querySelector("[name = 'phone']").value = ''
		input.querySelector("[name = 'target']").value = ''
	} catch(e){}

	try{
		document.getElementById('subcat').style.display = 'initial'
	} catch(e){}
})

form_cover.addEventListener('click', event => {
	form.style.display = 'none';
	form.style.opacity = 0
	input.querySelector("[name = 'image']").removeAttribute('required')
})
panel_cover.addEventListener('click', event => {
	panel = document.getElementById('subcategory-panel')
	panel.style.display = 'none';
	panel.style.opacity = 0
})


function editCategory(card, link){
	card = card.parentNode.parentNode

	form.style.display = 'flex';
	form.style.opacity = 1

	input = form.querySelector('form')
	input.setAttribute('action', link)

	input.querySelector("[name = 'name_uz']").value = card.querySelector('.card-name-uz').innerText
	input.querySelector("[name = 'name_ru']").value = card.querySelector('.card-name-ru').innerText
	input.querySelector("[name = 'name_en']").value = card.querySelector('.card-name-en').innerText

	document.getElementById('subcat').style.display = 'none'
	document.getElementById('subcategory').checked = false
	document.getElementById('parent').style.display = 'none'
}

function editProduct(card, link, id){
	product = products[id - 1]
	form.style.display = 'flex';
	form.style.opacity = 1

	input = form.querySelector('form')
	input.setAttribute('action', link)

	input.querySelector("[name = 'name_uz']").value = product['productName']['uz']['text']
	input.querySelector("[name = 'name_ru']").value = product['productName']['ru']['text']
	input.querySelector("[name = 'name_en']").value = product['productName']['eng']['text']

	input.querySelector("[name = 'desc_uz']").value = product['description']['uz']['text']
	input.querySelector("[name = 'desc_ru']").value = product['description']['ru']['text']
	input.querySelector("[name = 'desc_en']").value = product['description']['eng']['text']

	input.querySelector("[name = 'discount']").value = product['discount']
	input.querySelector("[name = 'price']").value = product['price']
	input.querySelector("[name = 'time']").value = Number(product['readyTime'].replace('min', ''))
}

function editBranch(card, link){
	card = card.parentNode.parentNode

	form.style.display = 'flex';
	form.style.opacity = 1

	input = form.querySelector('form')
	input.setAttribute('action', link)

	input.querySelector("[name = 'name_uz']").value = card.querySelector('#branch-name-uz').innerText
	input.querySelector("[name = 'name_ru']").value = card.querySelector('#branch-name-ru').innerText
	input.querySelector("[name = 'name_en']").value = card.querySelector('#branch-name-en').innerText

	input.querySelector("[name = 'phone']").value = card.querySelector('#branch-phone').innerText
	input.querySelector("[name = 'capacity']").value = card.querySelector('#branch-capacity').innerText
	input.querySelector("[name = 'target']").value = card.querySelector('#branch-target').innerText
}


function editSubCategory(id, link, token){
	form.style.display = 'flex';
	form.style.opacity = 1

	panel = document.getElementById('subcategory-panel')
	panel.style.display = 'none';
	panel.style.opacity = 0

	input = form.querySelector('form')
	input.setAttribute('action', link)

	input.style.display = 'none'
	document.getElementById('loading').style.display = 'initial'

	fetch(
		`http://admin.motitashkent.uz/api/v1/category/${id}`,
		{
			headers: {
				'Content-Type': 'application/json',
				'Authorization': token
			}
		}
	).then(response => response.json()).then(data => {
		input.querySelector("[name = 'name_uz']").value = data.categoryName.uz.text
		input.querySelector("[name = 'name_ru']").value = data.categoryName.ru.text
		input.querySelector("[name = 'name_en']").value = data.categoryName.eng.text

		document.getElementById('loading').style.display = 'none'
		input.style.display = 'block'

		document.getElementById('subcat').style.display = 'initial'
		document.getElementById('subcategory').checked = true
		document.getElementById('parent').style.display = 'initial'
		document.getElementById('parent').value = data.subcategoryId
	})
}


function showChildren(token, button){
	document.getElementById('spinner').style.display = 'initial'
	document.getElementById('subcategory-table').innerHTML = ''
	panel = document.getElementById('subcategory-panel')
	panel.style.display = 'flex';
	panel.style.opacity = 1

	child = `
		<tr>
			<td><b>ID</b></td>
			<td><b>Parent</b></td>
			<td><b>UZ</b></td>
			<td></td>
		</tr>
	`

	fetch(
		`http://admin.motitashkent.uz/api/v1/category/category?categoryId=${button.getAttribute('data-id')}`,
		{
			headers: {
				'Content-Type': 'application/json',
				'Authorization': token
			}
		}
	).then(response => response.json()).then(data => {
		data.forEach(category => {
			child += `
				<tr>
					<td>${category.id}</td>
					<td>${category.parentId}</td>
					<td>${category.name}</td>
					<td>
						<a href="javascript:void(0);" onclick="editSubCategory(${category.id}, '${window.location.origin}/categories/update/${category.id}', '${token}')"><i class="fal fa-pen-to-square"></i>&ensp;<small>Edit</small></a>
						<a href="${window.location.origin}/categories/delete/${category.id}"><i class="fal fa-trash"></i>&ensp;<small>Delete</small></a>
					</td>
				</tr>
			`
		})
		document.getElementById('spinner').style.display = 'none'
		document.getElementById('subcategory-table').innerHTML = child
	})
}

function showParentSelector(box){
	if (box.checked){
		document.getElementById('parent').style.display = 'initial'
	} else {
		document.getElementById('parent').style.display = 'none'
	}
}