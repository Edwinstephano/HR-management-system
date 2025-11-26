<template>
	<div class="flex flex-col gap-5 w-full">
		<div class="flex flex-row justify-between items-center">
			<div class="text-lg text-gray-800 font-bold">{{ __("Upcoming Holidays") }}</div>
			<div
				v-if="holidays?.data?.length"
				id="open-holiday-list"
				class="text-sm text-gray-800 font-semibold cursor-pointer underline underline-offset-2"
				@click="isModalOpen = true"
			>
				{{ __("View All") }}
			</div>
		</div>

		<div class="flex flex-col bg-white rounded" v-if="upcomingHolidays?.length">
			<div
				class="flex flex-row flex-start p-4 items-center justify-between border-b"
				v-for="holiday in upcomingHolidays"
				:key="holiday.holiday_date"
			>
				<div class="flex flex-row items-center gap-3 grow">
					<FeatherIcon name="calendar" class="h-5 w-5 text-gray-500" />
					<div class="text-base font-normal text-gray-800">
						{{ __(holiday.description) }}
					</div>
				</div>
				<div class="text-base font-bold text-gray-800">
					{{ holiday.formatted_holiday_date }}
				</div>
			</div>
		</div>

		<EmptyState :message="__('You have no upcoming holidays')" v-else />
	</div>

	<ion-modal
		ref="modal"
		v-if="holidays?.data?.length"
		:is-open="isModalOpen"
		@didDismiss="isModalOpen = false"
		:initial-breakpoint="1"
		:breakpoints="[0, 1]"
	>
		<div class="bg-white w-full h-full flex flex-col sm:h-auto sm:max-h-[80vh] sm:max-w-2xl sm:rounded-lg overflow-hidden">
			<div class="flex flex-row items-center justify-between p-4 border-b sticky top-0 bg-white z-10">
				<span class="text-gray-900 font-bold text-lg">{{ __("Holiday List") }}</span>
				<Button variant="ghost" @click="isModalOpen = false">
					<FeatherIcon name="x" class="h-5 w-5 text-gray-500" />
				</Button>
			</div>
			<div class="flex-1 overflow-y-auto p-4">
				<div class="flex flex-col gap-4">
					<div
						v-for="holiday in holidays.data"
						:key="holiday.holiday_date"
						class="flex flex-row items-center justify-between w-full p-2 hover:bg-gray-50 rounded transition-colors"
					>
						<div class="flex flex-row items-center gap-3 grow">
							<FeatherIcon name="calendar" class="h-5 w-5 text-gray-500" />
							<div class="text-base font-normal text-gray-800">
								{{ __(holiday.description) }}
							</div>
						</div>
						<div
							:class="[
								'text-base font-bold whitespace-nowrap',
								holiday.is_upcoming ? 'text-gray-800' : 'text-gray-500',
							]"
						>
							{{ holiday.formatted_holiday_date }}
						</div>
					</div>
				</div>
			</div>
		</div>
	</ion-modal>
</template>

<script setup>
import { inject, computed, ref } from "vue"
import { IonModal } from "@ionic/vue"
import { FeatherIcon, createResource } from "frappe-ui"

const employee = inject("$employee")
const dayjs = inject("$dayjs")
const __ = inject("$translate")
const modal = ref(null)
const isModalOpen = ref(false)

const holidays = createResource({
	url: "hrms.api.get_holidays_for_employee",
	params: {
		employee: employee.data.name,
	},
	auto: true,
	transform: (data) => {
		return data.map((holiday) => {
			const holidayDate = dayjs(holiday.holiday_date)
			holiday.is_upcoming = holidayDate.isAfter(dayjs())
			holiday.formatted_holiday_date = holidayDate.format("ddd, D MMM YYYY")
			return holiday
		})
	},
})

const upcomingHolidays = computed(() => {
	const filteredHolidays = holidays.data?.filter(
		(holiday) => holiday.is_upcoming
	)

	// show only 5 upcoming holidays
	return filteredHolidays?.slice(0, 5)
})
</script>
