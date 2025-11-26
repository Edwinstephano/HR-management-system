<template>
	<ion-page>
		<div class="flex flex-row h-screen w-full">
			<DesktopSidebar />
			<div class="flex-1 flex flex-col h-full overflow-hidden relative">
				<ion-tabs>
					<ion-router-outlet></ion-router-outlet>
					<BottomTabs class="md:hidden" />
				</ion-tabs>
			</div>
		</div>
	</ion-page>
</template>

<script setup>
import { IonTabs, IonPage, IonRouterOutlet } from "@ionic/vue"
import BottomTabs from "@/components/BottomTabs.vue"
import DesktopSidebar from "@/components/DesktopSidebar.vue"
</script>
