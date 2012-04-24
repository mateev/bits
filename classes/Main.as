package 
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.utils.getQualifiedClassName;
	import flash.utils.getDefinitionByName;
	
	public class Main extends Sprite 
	{
		
		public function Main():void 
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);

			var a:Array = new Array();
			
			a.push(test(1.3)(12));
			a.push(test(12)(0));
			a.push(test(12)(1));
			a.push(test(12.1)(0));
						
			for each(var elem:* in a)
				trace(elem);

			/* #Output:
					12
					false
					true
					0
			*/
		}
		
		private function test(e:*):Class
		{
			if (getQualifiedClassName(e) == getQualifiedClassName(Number))
				return int;
					
			return (getDefinitionByName("Boolean") as Class);
		}
		
	}
	
}