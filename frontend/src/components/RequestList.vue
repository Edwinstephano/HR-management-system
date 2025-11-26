<template>
	<div class="flex flex-col bg-white rounded-lg shadow-sm border border-gray-100 mt-5 overflow-hidden" v-if="props.items?.length">
		<div
			class="flex flex-row p-4 items-center justify-between border-b border-gray-100 cursor-pointer hover:bg-gray-50 transition-colors duration-150 last:border-b-0"
			v-for="link in props.items"
			:key="link.name"
			@click="openRequestModal(link)"
		>
			<component
				:is="props.component || link.component"
				:doc="link"
				:workflowStateField="link.workflow_state_field"
				:isTeamRequest="props.teamRequests"
			/>
		</div>

		<router-link
			v-if="props.addListButton"
			:to="{ name: props.listButtonRoute }"
			v-slot="{ navigate }"
		>
			<Button
				variant="ghost"
				@click="navigate"
				class="w-full !text-gray-600 py-6 text-sm border-none bg-white hover:bg-white"
			>
				{{ __("View List") }}
			</Button>
		</router-link>
	</div>
	<EmptyState :message="emptyStateMessage || __('You have no requests')" v-else />

	<ion-modal
		ref="modal"
		:is-open="isRequestModalOpen"
		@didDismiss="closeRequestModal"
		:initial-breakpoint="1"
		:breakpoints="[0, 1]"
	>
		<RequestActionSheet :fields="fieldsMap[selectedRequest?.doctype]" v-model="selectedRequest" />
	</ion-modal>
</template>

<script setup>
import { ref, inject } from "vue"
import { IonModal } from "@ionic/vue"
import RequestActionSheet from "@/components/RequestActionSheet.vue"

import {
	LEAVE_FIELDS,
	EXPENSE_CLAIM_FIELDS,
	ATTENDANCE_REQUEST_FIELDS,
	SHIFT_REQUEST_FIELDS,
	SHIFT_FIELDS,
} from "@/data/config/requestSummaryFields"

const __ = inject("$translate")
const props = defineProps({
	component: {
		type: Object,
	},
	items: {
		type: Array,
	},
	teamRequests: {
		type: Boolean,
		default: false,
	},
	addListButton: {
		type: Boolean,
		default: false,
	},
	listButtonRoute: {
		type: String,
		default: "",
	},
	emptyStateMessage: {
		type: String,
		default: "",
	},
})

const fieldsMap = {
	"Leave Application": LEAVE_FIELDS,
	"Expense Claim": EXPENSE_CLAIM_FIELDS,
	"Attendance Request": ATTENDANCE_REQUEST_FIELDS,
	"Shift Request": SHIFT_REQUEST_FIELDS,
	"Shift Assignment": SHIFT_FIELDS,
}

const isRequestModalOpen = ref(false)
const selectedRequest = ref(null)

const openRequestModal = async (request) => {
	selectedRequest.value = request
	isRequestModalOpen.value = true
}

const closeRequestModal = async () => {
	isRequestModalOpen.value = false
	selectedRequest.value = null
}
</script>
