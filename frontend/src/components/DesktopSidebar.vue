<template>
	<aside
		class="hidden md:flex flex-col w-64 bg-white border-r border-gray-200 h-screen sticky top-0"
	>
		<div class="h-14 flex items-center px-5 border-b border-gray-100">
			<div class="text-lg font-bold text-gray-800">Frappe HR</div>
		</div>
		<nav class="flex-1 overflow-y-auto py-6 px-3 space-y-1">
			<router-link
				v-for="item in tabItems"
				:key="item.title"
				:to="item.route"
				class="flex items-center gap-3 px-3 py-2 rounded-md transition-colors"
				:class="[
					route.path === item.route
						? 'bg-gray-100 text-gray-900'
						: 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
				]"
			>
				<component
					:is="item.icon"
					class="w-4 h-4"
					:class="[
						route.path === item.route
							? 'text-gray-900'
							: 'text-gray-500',
					]"
				/>
				<span class="font-medium">{{ item.title }}</span>
			</router-link>
		</nav>
		<div class="p-4 border-t border-gray-100">
			<div class="flex items-center gap-3 px-3 py-2">
				<Avatar :image="user.data?.user_image" :label="user.data?.full_name" size="sm" />
				<div class="flex flex-col overflow-hidden">
					<div class="text-sm font-medium text-gray-900 truncate">
						{{ user.data?.full_name }}
					</div>
					<div class="text-xs text-gray-500 truncate">
						{{ user.data?.email }}
					</div>
				</div>
			</div>
		</div>
	</aside>
</template>

<script setup>
import { inject } from "vue"
import { useRoute } from "vue-router"
import { Avatar } from "frappe-ui"

import HomeIcon from "@/components/icons/HomeIcon.vue"
import LeaveIcon from "@/components/icons/LeaveIcon.vue"
import ExpenseIcon from "@/components/icons/ExpenseIcon.vue"
import SalaryIcon from "@/components/icons/SalaryIcon.vue"
import AttendanceIcon from "@/components/icons/AttendanceIcon.vue"

const __ = inject("$translate")
const user = inject("$user")
const route = useRoute()

const tabItems = [
	{
		icon: HomeIcon,
		title: __("Home"),
		route: "/home",
	},
	{
		icon: AttendanceIcon,
		title: __("Attendance"),
		route: "/dashboard/attendance",
	},
	{
		icon: LeaveIcon,
		title: __("Leaves"),
		route: "/dashboard/leaves",
	},
	{
		icon: ExpenseIcon,
		title: __("Expenses"),
		route: "/dashboard/expense-claims",
	},
	{
		icon: SalaryIcon,
		title: __("Salary"),
		route: "/dashboard/salary-slips",
	},
]
</script>
