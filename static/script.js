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


	try{
		input.querySelector("[name = 'image']").setAttribute('required', '')
		input.querySelector("[name = 'capacity']").value = ''
		input.querySelector("[name = 'phone']").value = ''
		input.querySelector("[name = 'target']").value = ''
	} catch(e){}

	try{
		document.getElementById('subcat').style.display = 'initial'
	} catch(e){}
})

try{
form_cover.addEventListener('click', event => {
	form.style.display = 'none';
	form.style.opacity = 0
	try{	
		input.querySelector("[name = 'image']").removeAttribute('required')
	} catch {}
})
panel_cover.addEventListener('click', event => {
	panel = document.getElementById('subcategory-panel')
	panel.style.display = 'none';
	panel.style.opacity = 0
})
} catch {}


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

	input.querySelector("[name = 'name_uz']").value = product['name']['uz']
	input.querySelector("[name = 'name_ru']").value = product['name']['ru']
	input.querySelector("[name = 'name_en']").value = product['name']['en']
	input.querySelector("[name = 'code']").value = product['code']

	input.querySelector("[name = 'desc_uz']").value = product['description']['uz']
	input.querySelector("[name = 'desc_ru']").value = product['description']['ru']
	input.querySelector("[name = 'desc_en']").value = product['description']['en']

	input.querySelector("[name = 'discount']").value = product['discount']
	input.querySelector("[name = 'price']").value = product['price']
	input.querySelector("[name = 'time']").value = product['readyTime']
	input.querySelector("[name = 'category']").value = product['categoryId']
}

function editBranch(card, link){
	card = card.parentNode.parentNode
	console.log(card.querySelector('#branch-address-name'))

	form.style.display = 'flex';
	form.style.opacity = 1

	input = form.querySelector('form')
	input.setAttribute('action', link)

	input.querySelector("[name = 'name_uz']").value = card.querySelector('#branch-name-uz').innerText
	input.querySelector("[name = 'name_ru']").value = card.querySelector('#branch-name-ru').innerText
	input.querySelector("[name = 'name_en']").value = card.querySelector('#branch-name-en').innerText

	input.querySelector("[name = 'district']").value = card.querySelector('#branch-address-district').innerText
	input.querySelector("[name = 'address_name']").value = card.querySelector('#branch-address-name').innerText
	input.querySelector("[name = 'street']").value = card.querySelector('#branch-address-street').innerText
	input.querySelector("[name = 'latitude']").value = card.querySelector('#branch-address-latitude').innerText
	input.querySelector("[name = 'longitude']").value = card.querySelector('#branch-address-longitude').innerText

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
		`http://admin.motitashkent.uz/api/v1/category/admin/${id}`,
		{
			headers: {
				'Content-Type': 'application/json',
				'Authorization': token
			}
		}
	).then(response => response.json()).then(data => {
		console.log(data)
		input.querySelector("[name = 'name_uz']").value = data.name.uz
		input.querySelector("[name = 'name_ru']").value = data.name.ru
		input.querySelector("[name = 'name_en']").value = data.name.en

		document.getElementById('loading').style.display = 'none'
		input.style.display = 'block'

		document.getElementById('subcat').style.display = 'initial'
		document.getElementById('subcategory').checked = true
		document.getElementById('parent').style.display = 'initial'
		document.getElementById('parent').value = data.parentCategoryId
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
			<td><b>Исходная категория</b></td>
			<td><b>Название</b></td>
			<td></td>
		</tr>
	`

	fetch(
		`http://admin.motitashkent.uz/api/v1/category/category?id=${button.getAttribute('data-id')}`,
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
					<td>${category.parentCategoryId}</td>
					<td>${category.name}</td>
					<td>
						<a href="javascript:void(0);" onclick="editSubCategory(${category.id}, '${window.location.origin}/categories/update/${category.id}', '${token}')"><i class="fal fa-pen-to-square"></i>&ensp;<small>Изменить</small></a>
						<a href="${window.location.origin}/categories/delete/${category.id}"><i class="fal fa-trash"></i>&ensp;<small>Удалить</small></a>
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