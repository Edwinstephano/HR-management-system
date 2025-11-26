<template>
	<div class="flex p-1 bg-gray-100 rounded-lg">
		<button
			v-for="button in buttons"
			:key="button.key ?? button.label ?? button"
			class="px-8 py-2.5 transition-all duration-200 rounded-md flex-auto font-medium text-sm"
			:class="
				modelValue === (button.key ?? button.label ?? button)
					? 'bg-white shadow-sm text-gray-900 ring-1 ring-black/5'
					: 'text-gray-500 hover:text-gray-700'
			"
			@click="$emit('update:modelValue', button.key ?? button.label ?? button)"
		>
			{{ button.label ?? __(button) }}
		</button>
	</div>
</template>

<script setup>
const props = defineProps({
	buttons: {
		type: Array,
		required: true,
	},
	modelValue: {
		type: String,
	},
})

defineEmits(["update:modelValue"])
</script>
