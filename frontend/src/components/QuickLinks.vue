<template>
	<div class="flex flex-col gap-5 my-4 w-full">
		<div class="text-lg font-medium text-gray-900">{{ title || __("Quick Links") }}</div>
		<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
			<router-link
				class="flex flex-row p-4 items-center justify-between bg-white rounded-lg shadow-sm border border-gray-100 hover:shadow-md hover:border-gray-200 transition-all duration-200 group"
				v-for="link in props.items"
				:key="link.title"
				:to="{ name: link.route }"
			>
				<div class="flex flex-row items-center gap-4 grow">
					<div
						class="h-10 w-10 rounded-full bg-gray-50 flex items-center justify-center group-hover:bg-gray-100 transition-colors"
					>
						<component
							:is="link.icon"
							class="h-5 w-5 text-gray-600 group-hover:text-gray-900 transition-colors"
						/>
					</div>
					<div
						class="text-base font-medium text-gray-700 group-hover:text-gray-900 transition-colors"
					>
						{{ link.title }}
					</div>
				</div>
				<FeatherIcon
					name="chevron-right"
					class="h-5 w-5 text-gray-400 group-hover:text-gray-600 transition-colors"
				/>
			</router-link>
		</div>
	</div>
</template>

<script setup>
import { FeatherIcon } from "frappe-ui"

const props = defineProps({
	title: {
		type: String,
		required: false,
		default: "",
	},
	items: {
		type: Array,
		required: true,
	},
})
</script>
