import random
import nodes
        
class VideoPromptGenerator:
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Doctor-Tools"

    @classmethod
    def IS_CHANGED(cls):
        return float("NaN")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {}),
                "adjectives": (
                    ["random"] + VideoPromptGenerator.ADJECTIVES,
                    {"default": "random"},
                ),
                "shot_type": (
                    ["random"] + VideoPromptGenerator.SHOT_TYPE,
                    {"default": "random"},
                ),
                "actions": (
                    ["random"] + VideoPromptGenerator.ACTIONS,
                    {"default": "random"},
                ),
                "style": (["random"] + VideoPromptGenerator.STYLE, {"default": "random"}),
                "director": (
                    ["random"] + VideoPromptGenerator.DIRECTOR,
                    {"default": "random"},
                ),
                "location": (["random"] + VideoPromptGenerator.LOCATION, {"default": "random"}),
                "modifiers": (["random"] + VideoPromptGenerator.MODIFIERS, {"default": "random"}),
                "lighting": (
                    ["random"] + VideoPromptGenerator.LIGHTING,
                    {"default": "random"},
                ),
            },
        }

    ADJECTIVES = [
        "",
	"bloody",
	"angry",
	"fat",
	"stoic",
	"old",
        "cool",
	"bearded",
	"happy",
	"vintage",
	"flaming",
        "icy",
    ]
    SHOT_TYPE = [
        "",
	"aerial shot:",
        "bird's-eye view:",
        "close-up:",
        "crane shot:",
        "fpv drone shot:",
        "dolly shot:",
        "dolly zoom left:",
        "dolly zoom right:",
        "dutch angle:",
        "establishing shot:",
        "extreme close-up:",
        "extreme long shot:",
        "eye-level shot:",
        "follow shot:",
        "high-angle shot:",
        "low-angle shot:",
        "medium close-up:",
        "medium shot:",
        "over-the-shoulder shot:",
        "pan left:",
        "pan right:",
        "point-of-view (POV) shot:",
        "pull-back shot:",
        "reaction shot:",
        "reverse-angle shot:",
        "tilt up:",
        "tilt down:",
        "tracking shot:",
        "two-shot:",
        "wide shot:",
    ]

    ACTIONS = [
        "",
        "crosses a street",
        "answering the phone",
        "driving a sports car",
        "shooting a gun",
        "screaming",
        "biting lip nervously",
        "blinking rapidly",
        "shrinking",
        "bursting into laughter",
        "checking their watch",
        "clapping hands excitedly",
        "crossing arms defiantly",
        "crying softly",
        "dancing gracefully",
        "drinking from a glass",
        "eating hurriedly",
        "falling to the ground",
        "frowning deeply",
        "gesturing wildly",
        "glancing sideways suspiciously",
        "grinning mischievously",
        "holding a banana up to their head like a phone",
        "looking around anxiously",
        "looking down in embarrassment",
        "looking up in awe",
        "looking surprised",
        "nodding in agreement",
        "pointing accusingly",
        "raising eyebrows in disbelief",
        "dancing",
        "running away from explosions",
        "scratching head in confusion",
        "shaking head in disbelief",
        "shivering from the cold",
        "shooting a shotgun",
        "sitting down slowly",
        "with a huge comic grin",
        "sneezing suddenly",
        "staring blankly",
        "crosses eyes",
        "starting to run",
        "doing jumping jacks",
        "stretching arms wide",
        "shooting a machine gun from the back of a pickup truck",
        "turning around quickly",
        "walking purposefully",
        "waving enthusiastically",
        "whispering a secret",
        "yawning sleepily",
        "jet sking",
        "crying in prison",
        "giving a thumbs up",
        "winking playfully",
        "skateboard oli down stairs",
        "loading a gun",
        "head blows up into an explosion of blood and gore",
        "rolling eyes",
        "crossing legs casually",
        "throws poop at the camera",
        "reaching out",
        "peeling of thier face",
        "playing russian roulette",
        "being chased by a killer",
        "on a skateboard",
        "holding a knife",
        "flying an airplane",
        "narrowing eyes suspiciously",
        "breaking open a door with an ax",
        "holding their head in pain",
        "sitting on a toilet",
        "running in circles",
        "throwing a fit like a baby",
        "snapping fingers",
        "giving a thumbs down",
    ]

    STYLE = [
        "",
	"cinematic",
        "cctv footage",
        "surrealism",
        "futurism",
        "1980s horror movie",
        "1990s hip hop video",
        "documentary",
        "futurism",
        "3D animation",
        "anime",
        "cartoon",
        "3D render",
        "2003 action movie",
        "music video",

    ]

    DIRECTOR = [
        "",
	"David Fincher",
        "Quentin Tarantino",
        "Martin Scorsese",
        "Steven Spielberg",
        "George Lucas",
    ]

    LOCATION = [
        "",
	"indoor",
        "outdoor",
        "at night",
        "in the park",
        "studio",
        "at a party",
        "at a festival",
        "at a concert",
        "on the moon",
        "infront of a magical portal with particles",
        "in a neon lit city",
        "in a cyberpunk city",
        "in a fantasy world",
        "at a fashion show",
        "in space",
        "in a dumpster",
        "on the streets of tokyo",
        "on a farm",
        "in a hospital",
        "in a prison",
        "in at the worlds fair",
        "inside the cockpit of a 474",
        "on top of a tractor trailer on the highway",
        "on the streets of new york city",
        "inside the chernobyl nuclear reactor",
        "on a space shuttle",
        "at home",
        "at work",
        "at a cafe",
        "at a gym",
        "at a hotel",
        "at a concert performance",
        "at the beach",
        "at a museum",
        "in a hidden city deep in the rainforest",
        "in a floating island in the sky",
        "in an underground world beneath the earths surface ",
        "in a secret garden hidden in a mysterious maze",
        "in a grand castle on the top of a remote mountain",
        "in a enchanted forest with talking animals and magical creatures",
        "in a mystical island filled with ancient ruins and hidden treasure",
        "in a faraway planet with a unique and alien landscape",
        "in a hidden paradise hidden behind a waterfall",
        "in a church",
        "in a hidden oasis in the desert",
        "in a secret underground city",
        "in an underwater kingdom",
        "in a lost temple in the jungle",
        "in a castle in the clouds",
        "in a hidden valley in the mountains",
        "in a alien city on a distant planet",
        "in a mystical land of eternal twilight",
        "infront of the USA flag",
        "in suburban america", 
        "in the suburbs", 
        "in the slums", 
        "at the sea", 
        "at the ocean",
        "at the lake",
        "at the river",
        "at the waterfall",
        "in the labyrinth",
        "in a lab"
    ]

    MODIFIERS = [
        "",
	"glitchy",
	"creepy",
	"abstract",
	"slow-motion",
	"static shot",
        "retro",
    ]

    LIGHTING = [
        "",
        "dramatic lighting",
        "shot at golden hour",
        "colorful lighting",
        "soft lighting",
        "studio lighting with strong rim light",
        "ambient lighting",
        "sun rays",
        "cinematic lighting",
        "volumetric lighting",
        "outdoor lighting",
        "soft pastel lighting colors scheme",
        "sensual lighting",
        "neon lights",
        "rim light, iridescent accents",
        "fantastic colors",
        "accent lighting",
        "high key lighting",
        "low key lighting",
        "strong backlight",
        "artificial lighting",
        "laser lighting",
        "multi-colored lighting",
        "mood lighting",
        "accent lighting",
        "bioluminiscent",
        "anamorphic lens flare",
        "atmospheric",
        "cinematic sensual",
        "glow effect",
        "shallow depth of field",
        "hdr",
        "dynamic composition",
        "broad light",
        "natural lighting",
        "beautiful dynamic dramatic dark moody lighting",
        "flat color scheme",
        "(muted colors, dim colors, soothing tones:1.3), low saturation, (hyperdetailed:1.2)",
        "(noir:0.4), (intricate details:1.12), hdr, (intricate details, hyperdetailed:1.15)",
    ]
    @staticmethod
    def generate_prompt(**kwargs):
        components = []

        # Get shot type (first in the prompt)
        shot_type = kwargs.get("shot_type", "")
        if shot_type.lower() == "random":
            shot_type = random.choice(VideoPromptGenerator.SHOT_TYPE)
        components.append(shot_type)

        # Get adjectives (to appear before subject in the prompt)
        adjectives = kwargs.get("adjectives", "")
        if adjectives.lower() == "random":
            adjectives = random.choice(VideoPromptGenerator.ADJECTIVES)
        components.append(adjectives)

        # Get subject (after adjectives in the prompt, first in the UI)
        subject = kwargs.get("subject", "")
        components.append(subject)

        # Get location
        location = kwargs.get("location", "")
        if location.lower() == "random":
            location = random.choice(VideoPromptGenerator.LOCATION)
        components.append(location)

        # Get style
        style = kwargs.get("style", "")
        if style.lower() == "random":
            style = random.choice(VideoPromptGenerator.STYLE)
        components.append(f"{style} style")

        # Get director
        director = kwargs.get("director", "")
        if director.lower() == "random":
            director = random.choice(VideoPromptGenerator.DIRECTOR)
        components.append(f"by {director}")

        # Get Modifiers (before lighting in the prompt)
        modifiers = kwargs.get("modifiers", "")
        if modifiers.lower() == "random":
            modifiers = random.choice(VideoPromptGenerator.MODIFIERS)
        components.append(modifiers)

        # Get lighting (last element in the prompt)
        lighting = kwargs.get("lighting", "")
        if lighting.lower() == "random":
            selected_lighting = ", ".join(random.sample(VideoPromptGenerator.LIGHTING, random.randint(2, 5)))
        else:
            selected_lighting = lighting
        components.append(selected_lighting)

        # Join components to form the final prompt
        prompt = " ".join(filter(None, components))
        print(f"AUTOPROMPT: {prompt}")
        return (prompt,)

# Mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "VideoPromptGenerator": VideoPromptGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VideoPromptGenerator": "Video Prompt Generator",
}